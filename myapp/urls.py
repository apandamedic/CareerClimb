from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('resume-advisor/', views.resume_advisor, name='resume_advisor'),
    path('addJobListing/', views.add_job, name='add_job'),  # Add Job URL
    path('editJobListing/', views.edit_job, name='edit_job'),  # Edit Job URL
    path('individualJobListing/', views.individual_job, name='individual_job'),  # Individual Job Listing URL
    # Comment these out until the views are created
    # path('wishlist/', views.wishlist, name='wishlist'),
    # path('applied/', views.applied, name='applied'),
    # path('interviewing/', views.interviewing, name='interviewing'),
    # path('offer/', views.offer, name='offer'),
]
