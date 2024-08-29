from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    rate = models.FloatField(default=0, null=True)
    count = models.IntegerField(default=0, null=True)

class CourseMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()

    




