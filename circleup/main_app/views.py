from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView

from .models import Circle




# Create your views here.

# Class Based Views
class CircleCreate(CreateView):
    model = Circle
    fields = ['title', 'creator', 'description', 'tags']

    # Interrupt normal form_valid functionality to assign user
    def form_valid(self, form):
        # Assign logged in user
        form.instance.user = self.request.user
        # Allow CreateView to continue
        return super().form_valid(form)
    
class CircleUpdate(UpdateView):
    model = Circle
    fields = ['title', 'creator', 'description', 'tags']

class CircleDelete(DeleteView):
    model = Circle
    success_url = "/circles"

# Function Views
def home(request):
    return HttpResponse('<h1> Hello /ᐠ｡‸｡ᐟ\ﾉ </h1>')

def about(request):
    return render(request, 'about.html')

def circles_index(request):
    circles = Circle.objects.all()
    return render(request, 'circles/index.html', { 'circles': circles })

def circle_detail(request, circle_id):
    circle= Circle.objects.get(id=circle_id)
    return render(request, 'circles/detail.html', { 'circle': circle })

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
