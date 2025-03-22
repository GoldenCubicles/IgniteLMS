from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# class UserProfile(models.Model):
#     ROLE_CHOICES = [
#         ('Admin', 'Admin'),
#         ('Teacher', 'Teacher'),
#         ('Student', 'Student'),
#     ]

#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=128)  # Store hashed passwords in production
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES)

#     def __str__(self):
#         return f"{self.username} ({self.role})"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords (use Django’s `make_password`)
    subject = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Teacher: {self.name} - {self.subject}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords (use Django’s `make_password`)
    grade = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Student: {self.name} - Grade {self.grade}"