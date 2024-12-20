from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import JobListing,JobDescription, Resume, InterviewQuestion
from .utils import generate_interview_questions
import chardet
from openai import OpenAI
from .forms import UserProfileForm
from .models import UserProfile
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

#profile

def profile(request):
    if request.user.is_authenticated:
        # Get the user's profile or create one if it doesn't exist
        profile, created = UserProfile.objects.get_or_create(user=request.user)

        if request.method == 'POST':
            
            form = UserProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.is_saved = True  
                profile.save()
                return redirect('profile')  # Redirect after saving
        else:
            form = UserProfileForm(instance=profile)

        return render(request, 'profile.html', {
            'form': form,
            'profile': profile,
            'is_authenticated': True,
        })

    # For unauthenticated users, show a default read-only profile
    return render(request, 'profile.html', {
        'form': None,
        'profile': None,
        'is_authenticated': False,
        'is_editable': False,
    })

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

        if deadline:
            deadline = datetime.strptime(deadline, '%Y-%m-%d').date()

        # Create a new job entry in the database
        job_listing = JobListing.objects.create(
            user = request.user,
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

        return redirect('individual_job_listing', job_id=job_listing.id)

    return render(request, 'addJobListing.html')

# Edit job listing view
def edit_job_listing(request, job_id):
    job = get_object_or_404(JobListing, id=job_id, user = request.user)

    if request.method == "POST":
        job.company_name = request.POST.get('company-name')
        job.job_title = request.POST.get('job-title')
        job.post_url = request.POST.get('post-url')
        job.location = request.POST.get('location')
        job.work_style = request.POST.get('work-style')
        job.salary = request.POST.get('salary')
        job.status = request.POST.get('status')

        # Convert the string date into a datetime.date object
        deadline_str = request.POST.get('deadline')
        if deadline_str:
            job.deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()

        job.contacts = request.POST.get('contacts')
        job.notes = request.POST.get('notes')
        job.save()
        return redirect('individual_job_listing', job_id=job.id)
    
    return render(request, 'editJobListing.html', {'job': job})

# Delete job listing view
def delete_job_listing(request, job_id):
    job = get_object_or_404(JobListing, id=job_id, user = request.user)
    # Delete the job object
    job.delete()

    # Redirect to dashboard after deletion
    return redirect('home')
    

# Individual job listing view
@login_required
def individual_job_listing(request, job_id):
    # Retrieve the job listing by ID
    job = get_object_or_404(JobListing, id=job_id, user = request.user)

    return render(request, 'individualJobListing.html', {'job': job})

#Login view
def login_view(request):
    if request.method == 'POST':
        email = request.POST['login-email']
        password = request.POST['login-password']

        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')  # Redirect to the 'profile' view or home page
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')  # Redirect back to the login page if login fails
    return render(request, 'login.html')

#Logout

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Redirect to the login page or homepage

#Register view
def register(request):
    if request.method == 'POST':
        first_name = request.POST['register-firstName']
        last_name = request.POST['register-lastName']
        email = request.POST['register-email']
        password1 = request.POST['register-password']
        password2 = request.POST['register-RePassword']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already registered as username')
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=email, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Automatically log in the user
        login(request, user)
        messages.success(request, 'Account created successfully')
        return redirect('home')  # Redirect to your homepage or dashboard
    return render(request, 'register.html')

#Forgot Password View
def forgotPassword(request):
    return render(request, 'forgotPassword.html')

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



#home page view
def home(request):
    wishlist_jobs = JobListing.objects.filter(user=request.user, status='wishlist')
    applied_jobs = JobListing.objects.filter(user=request.user, status='applied')
    offer_jobs = JobListing.objects.filter(user=request.user, status='offer')
    favorites_jobs = JobListing.objects.filter(user=request.user, status='favorites')
    follow_up_jobs = JobListing.objects.filter(user=request.user, status='follow-up')
    interviewing_jobs = JobListing.objects.filter(user=request.user, status='interviewing')

    # Pass job data to the template
    context = {
        'wishlist_jobs': wishlist_jobs,
        'applied_jobs': applied_jobs,
        'offer_jobs': offer_jobs,
        'favorites_jobs': favorites_jobs,
        'follow_up_jobs': follow_up_jobs,
        'interviewing_jobs': interviewing_jobs,
    }

    return render(request, 'home.html', context)