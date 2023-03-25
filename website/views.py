from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def home(request):
    # Check to see if logging in
    if request.method == "POST":
        username = request.POST['username']  # the key matches the name of the tag in the HTML
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in!")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in, \
                           please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.warning(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})
