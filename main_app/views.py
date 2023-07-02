from typing import Any, Dict
from django.shortcuts import render
from .models import PrimaryPlanet
from django.views.generic.base import TemplateView


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
            context['cars'] = PrimaryPlanet.objects.all()
        return context