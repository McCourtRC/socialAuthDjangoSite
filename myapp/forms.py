from django import forms
from .models import MyApp

class MyAppForm(forms.ModelForm):
    """form for MyAppForm"""
    #meta used for admin site
    class Meta:
        model = MyApp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email
