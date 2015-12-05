from django.conf import settings
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from . forms import TensorForm
from . forms import TestForm
from . models import  TensorModel

import tensorflow as tf

#import ipdb

IMAGE_WIDTH = 28
IMAGE_HEIGHT = 28
IMAGE_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT

TEST_FILE = settings.BASE_DIR + '/static/test/'

#[0,0,0,0,0,0,0,0,0,0]
LABEL_SIZE = 10


class VSuccessView(TemplateView):
    template_name = 'app/success.html'

class VCreateView(CreateView):
    model = TensorModel

    fields  = ['image','label',]

    def get_success_url(self):
        return reverse("app:success")

    def form_valid(self,form):
        # label code
        dic = { '0' : "[0,0,0,0,0,0,0,0,0,0]",
                '1' : "[0,1,0,0,0,0,0,0,0,0]",
                '2' : "[0,0,1,0,0,0,0,0,0,0]",
                '3' : "[0,0,0,1,0,0,0,0,0,0]",
                '4' : "[0,0,0,0,1,0,0,0,0,0]",
                '5' : "[0,0,0,0,0,1,0,0,0,0]",
                '6' : "[0,0,0,0,0,0,1,0,0,0]",
                '7' : "[0,0,0,0,0,0,0,1,0,0]",
                '8' : "[0,0,0,0,0,0,0,0,1,0]",
                '9' : "[0,0,0,0,0,0,0,0,0,1]",
        }
        form.instance.label_code = dic[form.instance.label]
        form.save()
        #image code

        image_path = settings.BASE_DIR + '/static/media/' + form.instance.image.name

        #f = tf.read_file(image_path)
        #with tf.Session() as session:
		#form.instance.image_code = session.run(f)
        form.instance.image_code = load_image(image_path,IMAGE_WIDTH,IMAGE_HEIGHT)

        form.save()

        return super(VCreateView,self).form_valid(form)



class VListView(ListView):
    queryset = TensorModel.objects.all()

class VDetailView(DetailView):
    pass


def handle_uploaded_file(f):
    filename = TEST_FILE+f.name
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def test(request):
    #ipdb.set_trace()
    result ="none"
    if request.method == 'POST':
        if request.FILES:
            f = request.FILES['testImage']
            handle_uploaded_file(f)
            #train()
            result = check(TEST_FILE + f.name)
        form = None
    else:
        form =  TestForm()
    return render(request,'app/tensormodel_test.html',{'form':form,'result':result})





# load image 
def load_image(filename,width,height):
    f = tf.read_file(filename)
    image = tf.image.decode_jpeg(f,channels=1)
    with tf.Session() as session:
        image = session.run(image)
        const1 = tf.constant(image)
        image_size = tf.image.resize_images(const1,width,height)
        image_size = tf.reshape(image_size,[1,width*height])
        image_size = session.run(image_size)
        return image_size
    
def check(filename):
  """ test image """
  #mnist = read_data_sets("MNIST_data",one_hot=True)
  mnist = TensorModel.objects.all()
  #ipdb.set_trace()
  #image 
  #1,2,3,4
  image = tf.placeholder("float",[None,784])
  
  #label
  #1,2,3,4,tensor 
  label = tf.placeholder("float",[None,10])
  
  w = tf.Variable(tf.zeros([784,10]))#input IMAGE_SIZE output 10
  b = tf.Variable(tf.zeros([10]))#input 10
  
  with  tf.Session() as session:
  
    y = tf.nn.softmax(tf.matmul(image,w)+b)
    
    
    cross_entryopy = -tf.reduce_sum(label*tf.log(y))
    
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entryopy)
    
    init = tf.initialize_all_variables()
    
    session.run(init)
    
    #for i in range(1000):
      #batch_xs,batch_ys = mnist.train.next_batch(100)
      #session.run(train_step, feed_dict={image: batch_xs, label: batch_ys})
    train_path = settings.BASE_DIR + "/static/media/"
    for r in mnist:
      image_code = load_image(train_path + r.image.name,IMAGE_WIDTH,IMAGE_HEIGHT)
      label_code = eval(r.label_code)
      label_code = session.run( tf.reshape(label_code,[1,10]) )
      session.run(train_step, feed_dict={image: image_code, label: label_code})
  
    check_image = tf.argmax(y,1)
    
    check_label = tf.argmax(label,1)
    
    #test 
    #img = [ mnist.test.images[2] ]
    #image = misc.imread('5.jpg')
    img = load_image(filename,IMAGE_WIDTH,IMAGE_HEIGHT)

    #image1 =misc.imresize(image,(28,28)) 
    #image1 = [image1.reshape([28*28]) ]
    #print(img[0])
    
    re =  session.run(check_image, feed_dict={image:img})
    return re
