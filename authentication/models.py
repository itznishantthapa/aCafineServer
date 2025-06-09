from django.db import models
from django.contrib.auth.models import AbstractUser

# Here i am going to create a models with the role based authentication seller,customer.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
    ('seller', 'Seller'),
    ('customer','Customer'),
    )
    role =models.CharField(max_length=20,choices=ROLE_CHOICES,default='customer')
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(unique=True)
    phone= models.CharField(max_length=15,blank=True,null=True)


