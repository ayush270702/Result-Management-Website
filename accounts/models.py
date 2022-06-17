from asyncio.windows_events import NULL
from operator import mod
from statistics import mode
from django.db import models

import email
from django.forms import CharField
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    organization = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=6, choices= [("Male","Male"), ("Female","female")], null=True)
    faculty = models.CharField(max_length=7, choices= [("teacher","teacher"), ('student',"student")], null=True)
    div = models.CharField(max_length=7, choices= [("A","A"), ('B',"B")], null=True, blank=True
    )

    
    def __str__(self):
        return self.user.username
    
class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=30, null=True)

    
    def __str__(self):
        return self.student.username


class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)      

    def __str__(self):
        return self.teacher.username


class Marks(models.Model):
    stud = models.OneToOneField(Student, on_delete=models.CASCADE)
    sub1 = models.IntegerField(null=True,default=NULL)
    sub2 = models.IntegerField(null=True,default=NULL)
    sub3 = models.IntegerField(null=True,default=NULL)

  