
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index,name='home'),
    path("about", views.about,name='about'),
    path("services", views.services,name='services'),
    path("contact", views.contact,name='contact'),
    path("contact/", views.contact,name='contact'),
    path("fighting_games", views.fighting_games,name='fighting_games'),
    path("racing_games", views.racing_games,name='racing_games'),
    path("adventure_games", views.adventure_games,name='adventure_games'),
    path("popular_games", views.popular_games,name='popular_games'),
    path("dawnload", views.dawnload,name='dawnload'),
    
]
