from django.db import models
from django.conf import settings

# Create your models here.
class TensorModel(models.Model):
    """for tensor model"""
    NUMBER_CHOICES = (
            ("0",0), ("1",1), ("2",2), ("3",3), ("4",4),
            ("5",5), ("6",6), ("7",7), ("8",8), ("9",9),
    )
    image = models.ImageField(upload_to="app/")
    image_code = models.TextField()
    label = models.CharField(max_length= 50,choices=NUMBER_CHOICES,default=None)
    label_code = models.TextField()









    
