from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    books = models.CharField(max_length=10, default="test") 

class Cultures(models.Model):
    name = models.CharField(max_length=100)
    cultureName = models.CharField(max_length=100)
    collector = models.CharField(max_length=100)
    photos = models.CharField(max_length=100)