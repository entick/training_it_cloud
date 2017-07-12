from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    courses = models.ManyToManyField('courses.Course')

    def fullname(self):
        return self.name + " " + self.surname

    def __str__(self):
        return self.name + " " + self.surname