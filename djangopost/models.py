from django.db import models

# Create your models here.

class Blogs(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    liked_by=models.CharField(max_length=50)