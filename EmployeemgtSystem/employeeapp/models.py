from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    empno = models.IntegerField()
    ename = models.CharField(max_length=20 , validators=[RegexValidator(regex=r'^[a-zA-Z/s]+$',
        message = 'Name can contain alphabets and spaces only',
        code = 'invaild_name')])
    email = models.CharField(max_length=50)
