from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import Task, Subtask
from home.utils import generate_subtasks_from_api
from django.shortcuts import get_object_or_404
import requests
from django.conf import settings
from .models import todo, todomonth, todoweek

def service2(request):
    data = todo.objects.all()
    return render(request, 'service2.html', {'data': data})

def add(request):
    tododata = request.POST['todo'] # Adds todo item
    todo_items = todo(content=tododata)
    todo_items.save()
    return redirect(service2)


def deleteItem(request, todo_id):
    item = todo.objects.get(id=todo_id)
    item.delete()
    return redirect(service2)


def week(request):
    dataweek = todoweek.objects.all()
    return render(request, 'week.html', {'dataweek': dataweek})

def addweek(request):
    tododata = request.POST['todoweek']
    todo_items = todoweek(content_week=tododata)
    todo_items.save()
    return redirect(week)

def deleteweek(request, todoweek_id):
    item = todoweek.objects.get(id=todoweek_id)
    item.delete()
    return redirect(week)


def month(request):
    datamonth = todomonth.objects.all()
    return render(request, 'month.html', {'datamonth': datamonth})

def addmonth(request):
    tododata = request.POST['todomonth']
    todo_items = todomonth(content_month=tododata)
    todo_items.save()
    return redirect(month)

def deletemonth(request, todomonth_id):
    item = todomonth.objects.get(id=todomonth_id)
    item.delete()
    return redirect(month)


def about(request):
    #return HttpResponse("this is about page")
    return render(request,'about.html')
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
    