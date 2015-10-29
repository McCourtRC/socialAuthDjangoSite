from django.contrib import admin

# Register your models here.
from .forms import MyAppForm
from .models import MyApp

class MyAppAdmin(admin.ModelAdmin):
    """Custom model admin view for Profile model"""
    list_display = ["__unicode__", "timestamp", "updated"]
    form = MyAppForm
    #class Meta:
    #    model = Profile


admin.site.register(MyApp, MyAppAdmin)
