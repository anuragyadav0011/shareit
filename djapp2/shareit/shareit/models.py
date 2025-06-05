from django.db import models

class Register(models.Model):
    regid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)            
    password=models.CharField(max_length=15)
    mobile=models.CharField(max_length=15)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    status=models.IntegerField()
    role=models.CharField(max_length=10)
    info=models.CharField(max_length=50)

class Sharenotes(models.Model):
    docid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    category=models.CharField(max_length=50)            
    description=models.CharField(max_length=500)
    filename=models.CharField(max_length=100)
    uid=models.CharField(max_length=50)
    info=models.CharField(max_length=50)

class Payment(models.Model):
    txnid=models.AutoField(primary_key=True)
    uid=models.CharField(max_length=50)
    amt=models.CharField(max_length=50)            
    info=models.CharField(max_length=50)