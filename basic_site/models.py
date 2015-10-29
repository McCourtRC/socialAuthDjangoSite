from django.db import models

# Create your models here.
class MyApp(models.Model):
    """Model for profile information"""
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #__str__ for Python 3
        return self.email
