from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                if User.objects.filter(username=username).exists():
                    messages.info(request, f"Yhe user with username {username} has been exists")
                else:
                    messages.info(request, f"Yhe user with username {username} has been registered")
            except User.DoesNotExist as error:
                return HttpResponse(error) #logger.error(error)
            form.save()
            messages.info(request, f'The user {username} has been registered')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context=context)


def login_user(request):
    # breakpoint()
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password do not match')
            # logger.info('Username or password do not match')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
