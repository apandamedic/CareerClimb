from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class JobListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    post_url = models.URLField()
    location = models.CharField(max_length=100)
    work_style = models.CharField(max_length=20, choices=[('hybrid', 'Hybrid'), ('on-site', 'On Site'), ('remote', 'Remote')])
    salary = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[
        ('wishlist', 'Wishlist'),
        ('applied', 'Applied'),
        ('interviewing', 'Interviewing'),
        ('follow-up', 'Follow Up'),
        ('offer', 'Offer')
    ])
    deadline = models.DateField()
    contacts = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job_title


class JobDescription(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        default = 2
        )  # Link to the user
    title = models.CharField(max_length=255)
    description = models.TextField()

class Resume(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()

class InterviewQuestion(models.Model):
    question = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('behavioral', 'Behavioral'),
        ('technical', 'Technical'),
        ('general', 'General')
    ])
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE, null=True, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, blank=True)
    
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    goal = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
# Automatically create or link UserProfile to User
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)  # Create profile if new user
    else:
        instance.userprofile.save()  # Update profile if user is updated