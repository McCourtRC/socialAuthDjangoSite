from django.shortcuts import render

from .forms import MyAppForm

# Create your views here.
def home(request):
    #add form
    form = MyAppForm(request.POST or None)
    if form.is_valid():
        pass
    context = {'form': form}
    return render(request, "home.html", context)

def about(request):
    context = {}
    return render(request, "about.html", context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)
