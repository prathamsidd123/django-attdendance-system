from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('subject/create/', views.create_subject, name='create_subject'),
    path('subject/<int:subject_id>/attendance/', views.take_attendance, name='take_attendance'),
    path('subject/<int:subject_id>/view/', views.view_attendance, name='view_attendance'),
]