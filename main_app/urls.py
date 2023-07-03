from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('primary_planets/', views.PlanetList.as_view(), name='planet_list'),
    path('primary_planets/new/', views.PlanetCreate.as_view(), name='planet_create'),
]