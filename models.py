from django.db import models

# Create your models here.

class logN(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)


class emploe(models.Model):
    emp_no=models.CharField(max_length=50)
    desg=models.CharField(max_length=50)
    fname=models.CharField(max_length=50) 
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    adrs1=models.CharField(max_length=50)
    adrs2=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pin=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    depart2=models.CharField(max_length=50)
    



class adminmodel(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)