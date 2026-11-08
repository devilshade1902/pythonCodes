from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField(max_length=3)
    name = models.CharField(max_length=20)