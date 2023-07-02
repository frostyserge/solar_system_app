from django.db import models

# Create your models here.
class PrimaryPlanet(models.Model):
    name = models.CharField(max_length=100)
    distance_from_sun = models.IntegerField(default=0)
    year_length = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    moons = models.IntegerField(default=0)
    
    def __str__(self):
        return self.distance_from_sun
    
    class Meta:
        ordering = ['distance_from_sun']
    