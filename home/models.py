from django.db import models

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
    content = models.TextField()

    def __str__(self):
        return self.content

class todoweek(models.Model):
    content_week = models.TextField()

    def __str__(self):
        return self.content_week

class todomonth(models.Model):
    content_month = models.TextField()

    def __str__(self):
        return self.content_month