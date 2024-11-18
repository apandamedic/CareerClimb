from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import JobListing,JobDescription, Resume, InterviewQuestion
from .utils import generate_interview_questions
import chardet
from openai import OpenAI
def profile(request):
    return render(request, 'profile.html')

def room(request):
    return HttpResponse('Room')

# Add job listing view
def add_job_listing(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        company_name = request.POST.get('company-name')
        job_title = request.POST.get('job-title')
        post_url = request.POST.get('post-url')
        location = request.POST.get('location')
        work_style = request.POST.get('work-style')
        salary = request.POST.get('salary')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        contacts = request.POST.get('contacts')
        notes = request.POST.get('notes')

    # Create a new job entry in the database
        JobListing.objects.create(
            company_name=company_name,
            job_title=job_title,
            post_url=post_url,
            location=location,
            work_style=work_style,
            salary=salary,
            status=status,
            deadline=deadline,
            contacts=contacts,
            notes=notes
        )

        # *********************** NEEDS TO BE EDITED ****************
        return redirect('profile')

    return render(request, 'addJobListing.html')

# Edit job listing view
def edit_job_listing(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)

    if request.method == "POST":
        job.company_name = request.POST.get('company-name')
        job.job_title = request.POST.get('job-title')
        job.post_url = request.POST.get('post-url')
        job.location = request.POST.get('location')
        job.work_style = request.POST.get('work-style')
        job.salary = request.POST.get('salary')
        job.status = request.POST.get('status')
        job.deadline = request.POST.get('deadline')
        job.contacts = request.POST.get('contacts')
        job.notes = request.POST.get('notes')
        job.save()
        return redirect('individual_job_listing', job_id=job.id)
    
    return render(request, 'editJobListing.html', {'job': job})

# Delete job listing view
def delete_job_listing(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    
    # Handle the deletion only if it's a POST request
    if request.method == 'POST':
        job.delete()
        # *********************** NEEDS TO BE EDITED ****************
        return redirect('DASHBOARD')  # Redirect to the job list or any other page
    
    # If not a POST request, return a confirmation page or the current page
    # *********************** NEEDS TO BE EDITED ****************
    return render('DASHBOARD')

# Individual job listing view
def individual_job_listing(request, job_id):
    # Retrieve the job listing by ID
    job = get_object_or_404(JobListing, id=job_id)

    return render(request, 'individualJobListing.html', {'job': job})

#Login view
def login(request):
    return render(request, 'login.html')

#Register view
def register(request):
    return render(request, 'register.html')

# the interview prep view
def interview_prep_view(request):
    if request.method == 'POST':
        job_description = request.POST.get('job_description')

        if not job_description:
            return render(request, 'error.html', {'message': "Please provide a job description to generate questions."})

        # Generate questions and format them
        raw_questions = generate_interview_questions(job_description)
        questions = format_questions(raw_questions)

        return render(request, 'interview_questions.html', {'questions': questions})

    return render(request, 'interview_prep_form.html')



def format_questions(response_text):
    """
    Format the response text into a list of questions for display.
    """
    questions = [{"category": "General", "question": line.strip()} for line in response_text.split("\n") if line.strip()]
    return questions
