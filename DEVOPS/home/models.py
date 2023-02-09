from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=122,null=True,blank=True)
    name=models.CharField(max_length=122,null=True,blank=True)
    ct=models.CharField(max_length=122,null=True,blank=True)
    num=models.CharField(max_length=122,null=True,blank=True)
    #desc=models.CharField(max_length=122,null=True)
    #date=models.DateField()
    
class Product(models.Model):
    pid=models.CharField(max_length=20,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    details=models.TextField(max_length=20000,null=True,blank=True)
    price=models.IntegerField()



    
    def __str__(self):
        return self.name