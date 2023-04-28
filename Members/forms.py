from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import *

class Lowercase(forms.CharField):
	def to_python(self,value):
		return value.lower()


class SupervisorRegistrationForm(UserCreationForm):
    first_name=forms.CharField(label='First Name',min_length=4,max_length=100,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],widget=forms.TextInput(attrs={'placeholder' : 'First Name',"class" : "form-control"}))

    last_name=forms.CharField(label='Last Name',min_length=4,max_length=100,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],widget=forms.TextInput(attrs={'placeholder' : 'Last Name',"class" : "form-control"}))

    username=forms.CharField(label="Username",widget=forms.TextInput(attrs={"placeholder" : "Enter A Username","class" : "form-control"}))

    email=Lowercase(label='Email Address',min_length=6,max_length=50,validators=[RegexValidator(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',message='Enter a Valid Email Address')],widget=forms.EmailInput(attrs={'placeholder' : 'Email' ,"class" : "form-control"}))

    password1 = forms.CharField(label='Password',widget=forms.TextInput(attrs={"placeholder" : "password1","type" : "password","class" : "form-control"}))

    password2 = forms.CharField(label='Confirm Your Password',widget=forms.TextInput(attrs={"placeholder" : "password2","type" : "password","class" : "form-control"}))
    
    group=forms.CharField(label='Entreprise Name',min_length=4,max_length=100,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],widget=forms.TextInput(attrs={'placeholder' : 'Entreprise Name',"class" : "form-control"}))

    class Meta:
        model = Supervisor
        fields = ['first_name','last_name','username','email','password1','password2',"group"]


class NormalRegistrationForm(UserCreationForm):
    first_name=forms.CharField(label='First Name',min_length=4,max_length=100,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],widget=forms.TextInput(attrs={'placeholder' : 'First Name',"class" : ""}))

    last_name=forms.CharField(label='Last Name',min_length=4,max_length=100,validators=[RegexValidator(r'^[a-zA-Z\s]*$',message="Only letters are allowed")],widget=forms.TextInput(attrs={'placeholder' : 'Last Name',"class" : "form__group"}))

    username=forms.CharField(label="Username",widget=forms.TextInput(attrs={"placeholder" : "Enter A Username","class" : "form__group"}))

    email=Lowercase(label='Email Address',min_length=6,max_length=50,validators=[RegexValidator(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',message='Enter a Valid Email Address')],widget=forms.EmailInput(attrs={'placeholder' : 'Email' ,"class" : "form__group"}))

    password1 = forms.CharField(label='Password',widget=forms.TextInput(attrs={"placeholder" : "password1","type" : "password","class" : "form__group"}))

    password2 = forms.CharField(label='Confirm Your Password',widget=forms.TextInput(attrs={"placeholder" : "password2","type" : "password","class" : "form__group"}))
    
    class Meta:
        model = Supervisor
        fields = ['first_name','last_name','username','email','password1','password2']