from django.db import models

# Create your models here.

class Sing_up(models.Model):
    name=models.CharField(max_length=80)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name




class Todo(models.Model):
    user=models.ForeignKey(Sing_up, on_delete=models.CASCADE)
    task=models.CharField(max_length=100)
    prio=models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.task
