from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('profile/')),  # Redirect root to profile
    path('profile/', views.profile, name='profile'),  # Profile page URL
    path('add-job/', views.add_job_listing, name='add_job'),

    # Edit job listing page URL
    path('edit-job/', views.edit_job_listing, name='edit_job'),

    # Individual job listing page URL
    path('job/', views.individual_job_listing, name='individual_job'),

    # Resume advisor page URL
    path('resume-advisor/', views.resume_advisor, name='resume_advisor'),

    #Login
    path('login/', views.login, name = 'login'),

    #Register
    path('register/', views.register, name = 'register'),
]
