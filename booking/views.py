from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from booking.forms import CreateUserForm


# Create your views here.
def index(request):
    return render(request, 'booking/index.html')


def users(request):
    users = User.objects.all()
    context = {'users': users}
    templatename = 'booking/users.html'
    return render(request, templatename, context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('schedule')  # replace 'home' with the name of your home page url
    context = {'form': form}
    return render(request, 'booking/register.html', context)


def schedule(request):
    templatename = 'booking/scehdule.html'
    context = {}
    return render(request, templatename, context)
