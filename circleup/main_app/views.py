from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from .models import Circle





# Create your views here.
def home(request):
    return HttpResponse('<h1> Hello /ᐠ｡‸｡ᐟ\ﾉ </h1>')

def about(request):
    return render(request, 'about.html')

def circles_index(request):
    circles = Circle.objects.all()
    return render(request, 'circles/index.html', { 'circles': circles })

def circle_detail(request, circle_id):
    circle= Circle.obects.get(id=circle_id)
    return render(request, 'circle/detail.html', { 'circle': circle })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid signup - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)