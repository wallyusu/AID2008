from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField('姓名', max_length=20, primary_key=True)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=11, default='')
    email = models.EmailField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

