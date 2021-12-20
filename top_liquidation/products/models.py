from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200, default='electronics')
    image = models.CharField(max_length=200, default='electronics')
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass