from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if a user with the provided email already exists
        if User.objects.filter(email=email).exists():
            message = 'Пользователь с таким Email уже существует'
            return render(request, 'registration.html', {'message': message})

        # Check if passwords match
        if password == password2:
            try:
                user = User.objects.create_user(username=email, email=email, password=password)
                if email == 'admin@gmail.com':
                    user.is_staff = True
                    user.is_superuser = True
                user.save()
                user = authenticate(username=email, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("/")
            except:
                message = 'Ошибка регистрации'
                return render(request, 'registration.html', {'message': message})
        else:
            message = 'Пароли не совпадают'
            return render(request, 'registration.html', {'message': message})
    else:
        return render(request, 'registration.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            message = 'Неверный логин или пароль'
            return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect("/")
