from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Login(models.Model):
    user_type=models.CharField(max_length=30)
    view_password=models.CharField(max_length=50)
    view_email=models.CharField(max_length=50)

    
class Customer(models.Model):
    username = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, null= True)
    email = models.EmailField(max_length=30,null=True)
    phone = models.CharField(max_length=30, null= True)
    image = models.FileField(null= True)
    
class Request(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    caption = models.CharField(max_length=250, null= True)
    description = models.CharField(max_length=300, null= True)
    platform = models.CharField(max_length=50, null= True)
    startDate = models.DateField()
    endDate = models.DateField()
    price =models.CharField(max_length=100, null= True)
    location = models.CharField(max_length=100, null= True)
    prefered_age_group = models.CharField(max_length=30, null= True)
    adimage = models.FileField(null= True)
    keywords = models.CharField(max_length=130, null= True)
    status  = models.CharField(max_length=20, default='requested')

class ConfirmedRequest(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    caption = models.CharField(max_length=250, null= True)
    description = models.CharField(max_length=300, null= True)
    platform = models.CharField(max_length=50, null= True)
    startDate = models.DateField()
    endDate = models.DateField()
    price =models.CharField(max_length=100, null= True)
    location = models.CharField(max_length=100, null= True)
    prefered_age_group = models.CharField(max_length=30, null= True)
    adimage = models.FileField(null= True)
    keywords = models.CharField(max_length=130, null= True)
    paymentstatus  = models.CharField(max_length=20, default='amount not added')

class Adminreport(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    ConfirmedRequest = models.ForeignKey(ConfirmedRequest, on_delete=models.CASCADE, null=True)
    like = models.CharField(max_length=100, null= True)
    comment = models.CharField(max_length=100, null= True)
    share = models.CharField(max_length=100, null= True)
    linkBasedinteraction = models.CharField(max_length=100, null= True)
    keywordBasedinteraction = models.CharField(max_length=100, null= True)
    ageBasedinteraction = models.CharField(max_length=100, null= True)

