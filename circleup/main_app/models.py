from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Circle(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    link = models.URLField(max_length=500)
    description = models.TextField()
    tags = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    allowed = models.ManyToManyField(User, related_name='allowed')  
    requested = models.ManyToManyField(User, related_name='requested')

    def __str__(self):
        return self.title