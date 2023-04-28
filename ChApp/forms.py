from django.forms import ModelForm
from django import forms
from django.core.validators import RegexValidator
from .models import *


class FileForm(ModelForm):
    file = forms.FileField()
    title=forms.CharField(label='File Name',min_length=4,max_length=100,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],widget=forms.TextInput(attrs={'placeholder' : 'File Name',"class" : "form-control"}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Description', "class": "form-control"}))
    class Meta:
        model = File
        fields = "__all__"
        exclude = ['user','created','updated','file_hash','file_id']



class FileModifyForm(ModelForm):
    #file = forms.FileField()
    #title=forms.CharField(label='File Name',min_length=4,max_length=100,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],widget=forms.TextInput(attrs={'placeholder' : 'File Name',"class" : "form-control"}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Description', "class": "form-control"}))
    class Meta:
        model = File
        fields = "__all__"
        exclude = ['user','created','updated','file_hash','file_id','title']
