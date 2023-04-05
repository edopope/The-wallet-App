
from django.db import models


# Create your models here.

class Account_User(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=200,blank=False,null=False)
    phoneNumber = models.IntegerField(blank=False, null=False)


