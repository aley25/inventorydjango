from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                password = form.cleaned_data['password']
            )
            user.save()
            return HttpResponseRedirect('login/', 200)

    else:
        form = SignupForm()
        return render(request, 'users/form.html', {'form': form})



def log(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): 
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/products/')
    else:
        form = LoginForm()
        return render(request, 'users/form.html', {'form': form, 'url': 'login/'})

