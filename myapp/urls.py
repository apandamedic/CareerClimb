from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),  
    path('add/', views.add_job_listing, name='add_job_listing'),
    path('edit/<int:job_id>/', views.edit_job_listing, name='edit_job_listing'),
    path('delete-job/<int:job_id>/', views.delete_job_listing, name='delete_job_listing'),
    path('job/<int:job_id>/', views.individual_job_listing, name='individual_job_listing'),
    path('interview_prep_form/', views.interview_prep_view, name='interview_prep_form'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name = 'register'),
    path('home/', views.home, name='home'),
    path('forgotPassword/', views.forgotPassword, name = 'forgot-password'),
]
