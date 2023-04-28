from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class Home(View):
    @method_decorator(login_required(login_url="login"))
    def dispatch(self,*args,**kwargs):
        return super().dispatch(*args,**kwargs)
    
    def get(self,request,*args,**kwargs):
        return render(request,'Core/home.html')