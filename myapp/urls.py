from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('profile/')), 
    path('profile/', views.profile, name='profile'),  
    path('add-job/', views.add_job_listing, name='add_job'),
    path('edit-job/', views.edit_job_listing, name='edit_job'),
    path('job/', views.individual_job_listing, name='individual_job'),
    path('resume-advisor/', views.resume_advisor, name='resume_advisor'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
]
