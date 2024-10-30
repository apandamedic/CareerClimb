from django.shortcuts import render

def profile(request):
    return render(request, 'myapp/templates/profile.html')

