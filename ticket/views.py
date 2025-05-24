from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import Ticket


def get_index(request):
    return render(request, 'ticket/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'ticket/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm
    return render(request, 'ticket/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'ticket/profile.html')


@login_required
def logout(request):
    return render(request, 'ticket/logout.html')




def get_ticket(request):
    tickets = Ticket.objects.filter(is_available=True).order_by('date')
    return render(request, 'ticket/index.html', {'tickets': tickets})




