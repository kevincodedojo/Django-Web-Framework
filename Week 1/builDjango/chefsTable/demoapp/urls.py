from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('home/', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('drinks/<str:drink_name>', views.drinks, name="drinks"),

    path('menu/', views.menu, name='menu'),

    path('booking/', views.booking, name='booking'),

    path('contact/', views.contact, name='contact'),

    
]