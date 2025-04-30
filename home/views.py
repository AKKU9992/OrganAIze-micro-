from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from datetime import datetime, timedelta
from home.models import Contact
from django.contrib import messages
from home.models import Task, Subtask
from home.utils import generate_subtasks_from_api
from django.shortcuts import get_object_or_404
import requests
from django.conf import settings
from home.models import todo, todomonth, todoweek
now = datetime.now()
from django.utils import timezone

now = timezone.now()
def service2(request):
    # Fetch all daily tasks
    data = todo.objects.all()
    
    # Loop through each task and calculate remaining time
    # for item in data:
    #     end_time = item.created_at + timedelta(minutes=item.duration_minutes)  # Assuming 'duration_minutes' is how long the task takes
    #     item.time_left = (end_time - datetime.now()).seconds // 60  # Convert remaining time to minutes
    #     item.time_left = max(item.time_left, 0)  # Ensure no negative values

    return render(request, 'service2.html', {'data': data})


def add(request):
    if request.method == 'POST':
        content = request.POST['todo']
        duration = int(request.POST['duration_minutes'])
        todo_items = todo(content=content, duration_minutes=duration)
        todo_items.save()
    return redirect('service2')


def deleteItem(request, todo_id):
    item = get_object_or_404(todo, id=todo_id)
    item.delete()
    return redirect('service2')


def week(request):
    dataweek = todoweek.objects.all()
    for item in dataweek:
        end_date = item.created_at + timedelta(days=item.duration_days)
        item.days_left = (end_date - timezone.now()).days  # FIXED LINE
        item.days_left = max(item.days_left, 0)  # Ensure no negative values

    return render(request, 'week.html', {'dataweek': dataweek})
def addweek(request):
    if request.method == 'POST':
        content = request.POST['content_week']
        task = request.POST['task']
        duration = int(request.POST['duration_days'])
        todo_items = todoweek(content_week=content, task=task, duration_days=duration)
        todo_items.save()
    return redirect('week')

def deleteweek(request, todoweek_id):
    item = todoweek.objects.get(id=todoweek_id)
    item.delete()
    return redirect(week)


def month(request):
    datamonth = todomonth.objects.all()
    for item in datamonth:
        end_date = item.created_at + timedelta(days=item.duration_days)
        item.days_left = (end_date - timezone.now()).days
        item.days_left = max(item.days_left, 0)
    return render(request, 'month.html', {'datamonth': datamonth})

def addmonth(request):
    if request.method == 'POST':
        content = request.POST['content_month']  # Task name (content for the month)
        task = request.POST['task']  # Task description
        duration = int(request.POST['duration_days'])  # Duration in days
        
        # Create a new `todomonth` entry and save it to the database
        todo_items = todomonth(content_month=content, task=task, duration_days=duration)
        todo_items.save()
        
    return redirect('month') 

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
    