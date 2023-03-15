from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'booking/index.html')


def users(request):
    users = User.objects.all()
    context = {'users': users}
    templatename = 'booking/users.html'
    return render(request, templatename, context)
