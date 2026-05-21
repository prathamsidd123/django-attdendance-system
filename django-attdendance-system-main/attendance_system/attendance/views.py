from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from .models import CustomUser, Subject, Attendance
from .forms import CustomUserCreationForm, SubjectForm, AttendanceForm

def teacher_required(user):
    return user.is_authenticated and user.user_type == 'teacher'

def student_required(user):
    return user.is_authenticated and user.user_type == 'student'

def home(request):
    return render(request, 'attendance/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome {user.username}')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'attendance/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'attendance/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('home')

@login_required
def dashboard(request):
    if request.user.user_type == 'teacher':
        subjects = Subject.objects.filter(teacher=request.user)
        return render(request, 'attendance/teacher_dashboard.html', {'subjects': subjects})
    else:
        # Get attendance records for the student
        attendance_records = Attendance.objects.filter(student=request.user)
        return render(request, 'attendance/student_dashboard.html', {'attendance_records': attendance_records})

@login_required
@user_passes_test(teacher_required)
def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.teacher = request.user
            subject.save()
            messages.success(request, f'Subject "{subject.name}" created successfully!')
            return redirect('dashboard')
    else:
        form = SubjectForm()
    return render(request, 'attendance/create_subject.html', {'form': form})

@login_required
@user_passes_test(teacher_required)
def take_attendance(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id, teacher=request.user)
    students = CustomUser.objects.filter(user_type='student')
    
    if request.method == 'POST':
        date = request.POST.get('date')
        for student in students:
            is_present = request.POST.get(f'student_{student.id}') == 'on'
            attendance, created = Attendance.objects.get_or_create(
                student=student,
                subject=subject,
                date=date,
                defaults={'is_present': is_present}
            )
            if not created:
                attendance.is_present = is_present
                attendance.save()
        
        messages.success(request, f'Attendance for {subject.name} saved successfully!')
        return redirect('dashboard')
    
    return render(request, 'attendance/take_attendance.html', {
        'subject': subject,
        'students': students,
        'today': timezone.now().date()
    })

@login_required
@user_passes_test(teacher_required)
def view_attendance(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id, teacher=request.user)
    attendance_records = Attendance.objects.filter(subject=subject).order_by('-date', 'student__username')
    return render(request, 'attendance/view_attendance.html', {
        'subject': subject,
        'attendance_records': attendance_records
    })