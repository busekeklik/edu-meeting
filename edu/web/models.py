from django.db import models

class Meetings(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=100)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, null=True)

class Teachers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.CharField(max_length=100)

class Courses(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teachers', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    description = models.TextField()

