from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Subject, Attendance

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'password1', 'password2')

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'subject', 'date', 'is_present']