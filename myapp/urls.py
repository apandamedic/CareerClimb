from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('profile/')),  # Redirect root to profile
    path('profile/', views.profile, name='profile'),  # Profile page URL
]
