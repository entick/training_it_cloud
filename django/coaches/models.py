from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_bitrh = models.DateField()
    gender = models.CharField(max_length=6,choices=(
        ('M', 'Male'),
        ('F', 'Female')))
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def name(self):
        return self.user.first_name

    def surname(self):
        return self.user.last_name
