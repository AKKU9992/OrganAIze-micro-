from django.db import models
from datetime import timedelta
from django.utils import timezone  
# makemigrations - create changes and store in a File 
# migrate- apply the pending changes creaded by makemigrations
# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Subtask(models.Model):
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    average_duration_days = models.IntegerField()
    is_completed = models.BooleanField(default=False) 


class todo(models.Model):
    content = models.CharField(max_length=100)
    duration_minutes = models.IntegerField(default=0)  # Time limit in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def time_left(self):
        # Convert created_at to a timezone-aware datetime if it's naive
        if self.created_at.tzinfo is None:
            self.created_at = timezone.make_aware(self.created_at, timezone.get_current_timezone())
        
        # Calculate the end time based on created_at and duration_minutes
        end_time = self.created_at + timedelta(minutes=self.duration_minutes)
        
        # Calculate the time left in minutes (use timezone-aware datetime for both)
        time_left = end_time - timezone.now()
        
        # If the time left is negative, return 0 minutes
        if time_left.total_seconds() < 0:
            return 0
        return time_left.total_seconds() // 60  # Return the time left in minutes



class todoweek(models.Model):
    content_week = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    duration_days = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Add this line

    def __str__(self):
        return self.content_week

from django.db import models

class todomonth(models.Model):
    content_month = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    duration_days = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # same as in todoweek

    def __str__(self):
        return self.content_month # 👈 Add this line

    def __str__(self):
        return self.content_month
    
task = models.CharField(max_length=255, default="Untitled Task")
