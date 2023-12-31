from django.db import models

# Create your models here.
class PrimaryPlanet(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    distance_from_sun = models.BigIntegerField(default=0)
    year_length = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    moons = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['distance_from_sun']

class Moon(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    year_of_discovery = models.IntegerField(default=0)
    discovered_by = models.CharField(max_length=150)
    planet = models.ForeignKey(PrimaryPlanet, on_delete=models.CASCADE, related_name='moon')

    def __str__(self):
        return self.name


    