from django.shortcuts import redirect,render
from django.views import View
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages


class SupervisorRegister(View):
    def get(self,request,*args,**kwargs):
        form = SupervisorRegistrationForm()
        context = {
            'form' : form,
        }
        return render(request,'Members/supervisor-normal-registration.html',context)

    def post(self,request,*args,**kwargs):
        form = SupervisorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_name = form.cleaned_data.get('group')
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            return redirect('home')
        
        context={
			'form' : form,
			
		}
        return render(request,'Members/supervisor-normal-registration.html',context)
    

class NormalRegister(View):
    def get(self,request,*args,**kwargs):
        form = NormalRegistrationForm()
        context = {
            'form' : form,
        }
        return render(request,'Members/supervisor-normal-registration.html',context)

    def post(self,request,*args,**kwargs):
        form = SupervisorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        context={
			'form' : form,
			
		}
        return render(request,'Members/supervisor-normal-registration.html',context)
    

class LoginUser(View):
    def get(self,request,*args,**kwargs):
        context={
			
		}
        return render(request, 'Members/login-user.html',context)

    def post(self,request,*args,**kwargs):
        username=request.POST['username']
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
        
        context={
			'form' : form,
			
		}
        return render(request,'Members/login-user.html',context)
       


