from django.db import models

# Create your models here.
class JobListing(models.Model):
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    post_url = models.URLField()
    location = models.CharField(max_length=255)
    work_style = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    deadline = models.DateField()
    contacts = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job_title