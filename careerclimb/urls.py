from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def profile(request):
    return HttpResponse('Profile Page')
    
urlpatterns = [
    path('admin/', admin.site.urls),  # For the admin interface
    path('', include('myapp.urls')),  # Includes URLs from the `myapp` app
]
