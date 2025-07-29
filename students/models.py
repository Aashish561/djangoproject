from django.db import models
from django.contrib.auth.models import AbstractUser

class DepartmentAdmin(AbstractUser):
    DEPARTMENTS = [
        ('BIT', 'Bachelor of IT'),
        ('BCS', 'Bachelor of CS'),
        ('BCA', 'Bachelor of CA'),
        ('CSIT', 'Bachelor of IT'),
        ('BHM', 'Bachelor of HM'),
    ]
    department = models.CharField(max_length=10, choices=DEPARTMENTS)

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=10, choices=DepartmentAdmin.DEPARTMENTS)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_by = models.ForeignKey(DepartmentAdmin, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.student_id})"