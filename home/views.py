from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
   if request.user.is_anonymous:
      return redirect("/login")
   return render(request,'index.html')
    
def loginuser(request):
   if request.method=="POST":
      username=request.POST.get("username")
      password=request.POST.get("password")
      print(username,password)
      #   check if user has enterect correct credentials
      user = authenticate(username=username, password=password)
      if user is not None:
          login(request,user)
        # A backend authenticated the credentials
          return redirect("/")
   
      else:
      
           return render(request,'login.html')

   return render(request,'login.html')

def logoutuser(request):
   logout(request)
   return redirect("/login")

def about(request):
    #return HttpResponse("this is about page")
    return render(request,'about.html')
def service1(request):
    return render(request,'service1.html')
    #return HttpResponse("this is services page")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your request has been sent!.")
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")
    