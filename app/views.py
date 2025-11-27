from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignupForm
from django.contrib.auth import authenticate, login

# Create your views here
def signup(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
    
    fm = SignupForm()
    return render(request, 'signup.html', {
        'form':fm
    })


def loginuser(request):
    if request.method == "POST":
        fm= AuthenticationForm(request=request, data= request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            paasword = fm.cleaned_data['password']
            user = authenticate(username=username, password= paasword)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/signup/')
    fm = AuthenticationForm()
    return render(request, 'login.html', {
        'form':fm
    })

