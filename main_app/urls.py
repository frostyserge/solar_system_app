from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('primary_planets/', views.PlanetList.as_view(), name='planet_list'),
    path('primary_planets/new', views.PlanetCreate.as_view(), name='planet_create'),
    path('primary_planets/<int:pk>/', views.PlanetDetail.as_view(), name='planet_detail'),
    path('primary_planets/<int:pk>/update', views.PlanetUpdate.as_view(), name='planet_update'),
    path('primary_planets/<int:pk>/delete', views.PlanetDelete.as_view(), name='planet_delete'),
]