from django.shortcuts import render,HttpResponse
from django.urls import reverse
from datetime import datetime
from home.models import Contact,Game
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
import uuid

# Create your views here.

# website related option start

def index(request):
    games=Game.objects.all()
    return render(request,'index.html',{'games':games})

def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email,phone=phone,desc=desc ,date=datetime.today())
        contact.save()
    return render(request,'contact.html')

# website related option end
# type of games start

def fighting_games(request):
    games=Game.objects.all()
    return render(request,'fighting_games.html',{'games':games})

def racing_games(request):
    games=Game.objects.all()
    return render(request,'racing_games.html',{'games':games})

def adventure_games(request):
    games=Game.objects.all()
    return render(request,'adventure_games.html',{'games':games})

def popular_games(request):
    games=Game.objects.all()
    return render(request,'popular_games.html',{'games':games})

def dawnload(request):
    return render(request,'dawnload.html')
# types of games end

