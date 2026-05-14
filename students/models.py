from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    GRADE_CHOICES = [
        ('A', 'Grade A'),
        ('B', 'Grade B'),
        ('C', 'Grade C'),
        ('D', 'Grade D'),
        ('F', 'Grade F'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    cgpa = models.FloatField(default=0.0)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, default='B')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    class Meta:
        ordering = ['roll_number']
        verbose_name_plural = 'Students'
    
    def __str__(self):
         return f"{self.user} - {self.roll_number}"
    

    