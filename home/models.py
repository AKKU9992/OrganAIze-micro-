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
    duration_minutes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def time_left(self):
        end_time = self.created_at + timedelta(minutes=self.duration_minutes)
        time_left = end_time - timezone.now()
        return max(0, int(time_left.total_seconds()))
class todoweek(models.Model):
    content_week = models.CharField(max_length=100)
    task = models.CharField(max_length=200)
    duration_days = models.IntegerField()
    completed = models.BooleanField(default=False)  # Set default to False if it’s a boolean field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content_week

    def time_left_seconds(self):
        end_time = self.created_at + timedelta(days=self.duration_days)
        time_left = end_time - timezone.now()
        return max(int(time_left.total_seconds()), 0)
    
from django.db import models

class todomonth(models.Model):
    content_month = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    duration_days = models.IntegerField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content_month

    def time_left_seconds(self):
        end_time = self.created_at + timedelta(days=self.duration_days)
        time_left = end_time - timezone.now()
        return max(int(time_left.total_seconds()), 0)
    
task = models.CharField(max_length=255, default="Untitled Task")
