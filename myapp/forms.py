from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
   class Meta:
       model = UserProfile
       fields = ['name', 'age', 'goal', 'bio', 'education', 'additional_info', 'resume']
