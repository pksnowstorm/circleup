from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse





# Create your views here.
def home(request):
    return HttpResponse('<h1> Hello /ᐠ｡‸｡ᐟ\ﾉ </h1>')

def about(request):
    return HttpResponse('<h1> About /ᐠ｡‸｡ᐟ\ﾉ </h1>')
