from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()

    fm = SignupForm()
    return render(request, 'signup.html', {
        'form':fm
    })