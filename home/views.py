from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from datetime import datetime, timedelta
from home.models import Contact,PriorityTask
from django.contrib import messages
from home.models import Task, Subtask
from django.shortcuts import get_object_or_404
import requests
from home.forms import TaskForm
from django.conf import settings
from home.models import todo, todomonth, todoweek
now = datetime.now()
from django.utils import timezone
from datetime import date
now = timezone.now()

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if not task.priority:
                task.priority = 'Low'
            task.save()
            return redirect('list')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})


def task_list(request):
    priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
    tasks = sorted(
        PriorityTask.objects.all(),
        key=lambda t: (priority_order.get(t.priority, 0), t.due_date if t.due_date else date.max)
    )
    return render(request, 'task.html', {'tasks': tasks})


def mark_as_done(request, task_id):
    task = get_object_or_404(PriorityTask, id=task_id)
    task.completed = True
    task.save()
    return redirect('list')







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
    dataweek = todoweek.objects.all().order_by('-created_at')
    for item in dataweek:
        item.time_left_seconds_val = item.time_left_seconds()
    return render(request, 'week.html', {'dataweek': dataweek})
def addweek(request):
    if request.method == 'POST':
        content_week = request.POST['content_week']
        task = request.POST['task']
        duration_days = int(request.POST['duration_days'])

        # Set a default value for 'completed' if it's not provided
        completed = False  # or request.POST.get('completed', False)

        todo_week = todoweek(content_week=content_week, task=task, duration_days=duration_days, completed=completed)
        todo_week.save()
        return redirect('week')  # Redirect after saving

def deleteweek(request, todoweek_id):
    item = todoweek.objects.get(id=todoweek_id)
    item.delete()
    return redirect(week)


def month(request):
    datamonth = todomonth.objects.all().order_by('-created_at')
    for item in datamonth:
        item.time_left_seconds_val = item.time_left_seconds()
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
    