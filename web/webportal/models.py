from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class Building(models.Model):
    manager = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    zip_code = models.IntegerField(default=0)

    def __str__(self):
        return self.name
