from django.db import models

# Create your models here.

class Post(models.Model):
    tittle=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    description=models.CharField(max_length=550)
    date=models.DateField(auto_now=False, auto_now_add=False,blank=True)
