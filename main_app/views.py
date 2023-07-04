from typing import Any, Dict
from django.urls import reverse
from django.shortcuts import redirect
from .models import PrimaryPlanet, Moon
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class PlanetList(TemplateView):
    template_name = 'planet_list.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        name = self.request.GET.get('name')
        if name != None:
            context['planets'] = PrimaryPlanet.objects.filter(name__icontains=name)
        else:
            context['planets'] = PrimaryPlanet.objects.all()
        return context
    
class PlanetCreate(CreateView):
    model = PrimaryPlanet
    fields = ['name', 'img', 'description', 'distance_from_sun', 'year_length', 'type', 'moons']
    template_name = 'planet_create.html'
    success_url = '/primary_planets/'

    def get_success_url(self):
        return reverse('planet_detail', kwargs={'pk': self.object.pk})

class PlanetDetail(DetailView):
    model = PrimaryPlanet
    template_name = 'planet_detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class PlanetUpdate(UpdateView):
    model = PrimaryPlanet
    fields = ['name', 'img', 'description', 'distance_from_sun', 'year_length', 'type', 'moons']
    template_name = 'planet_update.html'
    success_url = '/primary_planets/'

    def get_success_url(self):
        return reverse('planet_detail', kwargs={'pk': self.object.pk})
    
class PlanetDelete(DeleteView):
    model = PrimaryPlanet
    template_name = 'planet_confirm_delete.html'
    success_url = '/primary_planets/'

class MoonCreate(View):
    def post(self, request, pk):
        name = request.POST.get('name')
        img  = request.POST.get('img')
        description = request.POST.get('description')
        year_of_discovery = request.POST.get('year_of_discovery')
        discovered_by = request.POST.get('discovered_by')
        planet = PrimaryPlanet.objects.get(pk=pk)
        Moon.objects.create(name=name, img=img, description=description, year_of_discovery=year_of_discovery, discovered_by=discovered_by, planet=planet)
        return redirect('planet_detail', pk=pk)

