from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    names = models.TextField()
    coarse = models.CharField(max_length = 200)
    description = models.TextField(default='Good student')
    registration_date = models.DateField(default=datetime.date(2017,1,1))
    graduation_date = models.DateField(default=datetime.date(2017,12,1))
    def __str__ (self):
        return self.author