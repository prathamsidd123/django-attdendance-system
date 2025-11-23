from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    def __str__(self):
        return f"{self.username} ({self.user_type})"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'teacher'})
    
    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'student'})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('student', 'subject', 'date')
    
    def __str__(self):
        status = "Present" if self.is_present else "Absent"
        return f"{self.student.username} - {self.subject.name} - {self.date} - {status}"