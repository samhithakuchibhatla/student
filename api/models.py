from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER=[
    ('male','male'),
    ('female','female'),
    ]
    ACADEMIC=[
    ('higher','higher'),
    ('average','average'),
    ('lower','lower'),
    ]
    OBSERVE=[
    ('high','high'),

    ('low','low'),
    ]
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,choices=GENDER)
    academic=models.CharField(max_length=200,choices=ACADEMIC)
    observed=models.CharField(max_length=200,choices=OBSERVE)
    assess=models.CharField(max_length=10)
    def __str__(self):
        return self.name
