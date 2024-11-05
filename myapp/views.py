from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return render(request, 'profile.html')

def room(request):
    return HttpResponse('Room')

def add_job(request):
    return render(request, 'addJobListing.html')

def edit_job(request):
    return render(request, 'editJobListing.html')

def individual_job(request):
    return render(request, 'individualJobListing.html')

def resume_advisor(request):
    return render(request, 'ResumeAdvisor.html')

# Uncomment these when you are ready to use them
# def interviewing(request):
#     return render(request, 'interviewing.html')

# def offer(request):
#     return render(request, 'offer.html')
