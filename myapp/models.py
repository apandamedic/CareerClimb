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