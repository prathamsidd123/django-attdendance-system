# Django Attendance System

A simple Attendance Management System built with Django.  
This project allows teachers to manage subjects and attendance records while students can view their attendance dashboard.

---

# Features

- User Login & Registration
- Teacher Dashboard
- Student Dashboard
- Create Subjects
- Take Attendance
- View Attendance Records
- Admin Panel
- Responsive Templates

---

# Tech Stack

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite3

---

# Project Structure

```bash
django-attdendance-system/
│
├── attendance/
│   ├── migrations/
│   ├── templates/
│   │   └── attendance/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── teacher_dashboard.html
│   │       ├── student_dashboard.html
│   │       ├── create_subject.html
│   │       ├── take_attendance.html
│   │       └── view_attendance.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── attendance_system/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── venv/
```

---
# Navigate to directory
```bash
pratham@pratham-HP-EliteBook-840-G4:~/Downloads/Django_Attendence_Project_Github$ cd django-attdendance-system-main
pratham@pratham-HP-EliteBook-840-G4:~/Downloads/Django_Attendence_Project_Github/django-attdendance-system-main$ cd attendance_system

```
# Create Superuser

```bash
python manage.py createsuperuser
```

---

# Run Server

```bash
python manage.py runserver
```

---

# Open Browser

```bash
http://127.0.0.1:8000/
```

---

# Admin Panel

```bash
http://127.0.0.1:8000/admin/
```

---

# Screenshots

- Home Page
<img width="1920" height="1080" alt="Screenshot from 2026-05-21 19-38-22" src="https://github.com/user-attachments/assets/a5479b7e-0ef1-4d6d-b8f5-95530b25f719" />

- Login Page
<img width="1920" height="1080" alt="Screenshot from 2026-05-21 19-38-36" src="https://github.com/user-attachments/assets/093a17ba-85cc-4f96-b62e-5a327daac980" />

- Register Page
<img width="1920" height="1080" alt="Screenshot from 2026-05-21 19-38-41" src="https://github.com/user-attachments/assets/4a4c0c20-deb4-4154-ac8c-6f46b4de8bbe" />

- Teacher Dashboard
<img width="1920" height="1080" alt="Screenshot from 2026-05-21 20-11-37" src="https://github.com/user-attachments/assets/f1353232-6d9d-4ff4-9325-cae1e68cd900" />

- Student Dashboard
<img width="1920" height="1080" alt="Screenshot from 2026-05-21 20-11-11" src="https://github.com/user-attachments/assets/2e98396b-d9bc-42dc-ab21-7a997f121fb1" />

- Attendance Records
<img width="1920" height="1080" alt="Screenshot from 2026-05-21 20-11-55" src="https://github.com/user-attachments/assets/492b0e7c-6d0d-47c9-ae97-fda527742f24" />

---

# Future Improvements

- Attendance Percentage
- Export PDF Reports
- Email Notifications
- Better UI Design
- Search & Filters

---

# Author

Pratham Siddhpura


# License

This project is made for learning purposes.
