from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    coach = models.ForeignKey('coaches.Coach', related_name='coach_courses+', null=True, blank=True)
    assistant = models.ForeignKey('coaches.Coach', related_name='assistant_courses+', null=True, blank=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey('courses.Course')
    order = models.PositiveIntegerField(default=0, unique=False)

    def __str__(self):
        return self.subject

