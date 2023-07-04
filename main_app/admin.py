from django.contrib import admin
from .models import PrimaryPlanet, Moon

# Register your models here.
admin.site.register(PrimaryPlanet)
admin.site.register(Moon)

