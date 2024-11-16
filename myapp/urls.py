from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('profile/')), 
    path('profile/', views.profile, name='profile'),  
    path('add/', views.add_job_listing, name='add_job_listing'),
    path('edit/<int:job_id>/', views.edit_job_listing, name='edit_job_listing'),
    path('delete-job/<int:job_id>/', views.delete_job_listing, name='delete_job_listing'),
    path('job/<int:job_id>/', views.individual_job_listing, name='individual_job_listing'),
    path('resume-advisor/', views.resume_advisor, name='resume_advisor'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
]
