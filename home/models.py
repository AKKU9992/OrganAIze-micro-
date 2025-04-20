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