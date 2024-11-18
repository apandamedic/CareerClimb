from django.db import models

# Create your models here.
class JobListing(models.Model):
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
