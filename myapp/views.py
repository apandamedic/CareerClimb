from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return render(request, 'profile.html')

def room(request):
    return HttpResponse('Room')

# Add job listing view
def add_job_listing(request):
    return render(request, 'addJobListing.html')

# Edit job listing view
def edit_job_listing(request):
    return render(request, 'editJobListing.html')

# Individual job listing view
def individual_job_listing(request):
    return render(request, 'individualJobListing.html')

# Resume advisor view
def resume_advisor(request):
    return render(request, 'ResumeAdvisor.html')

#Login view
def login(request):
    return render(request, 'login.html')

#Register view
def register(request):
    return render(request, 'register.html')