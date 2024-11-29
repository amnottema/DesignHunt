from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if password == confirm_password:
            username = f'designer_{email[:3]}'
            user = User.objects.create_user(email=email, password=password, username=username)
            user.save()
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('create_portfolio')
        else:
            return render(request, 'authorization/authorization.html')
    return render(request, 'authorization/authorization.html')

def authorization(request):
    if request.user.is_authenticated:
        return redirect('create_portfolio')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_portfolio')
        else:
            return render(request, 'authorization/authorization.html')
    return render(request, 'authorization/authorization.html')


def logout_view(request):
    logout(request)
    return redirect('authorization')