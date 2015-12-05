from django import forms
from . models import  TensorModel


class TensorForm(forms.ModelForm):

    class Meta:
        model = TensorModel
        fields = ['image','label','label_code','image_code',]


class TestForm(forms.Form):
    testImage = forms.ImageField()
