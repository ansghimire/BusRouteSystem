from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Bus(models.Model):
    bus_name = models.CharField(max_length=264)
    bus_number = models.CharField(max_length=264)

    def __str__(self) -> str:
        return self.bus_name

    @property
    def all_route(self):
        return self.routes.all()
    
   

class Route(models.Model):
    bus = models.ManyToManyField(Bus, related_name='routes', through='TimeAssignModel')
    route = models.CharField(max_length=264)
    route_number = models.CharField(max_length=264)

    def __str__(self) -> str:
        return self.route

class TimeAssignModel(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    from_time = models.DateTimeField(default=timezone.now)
    to_time = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.bus} in {self.route} in time between {self.from_time} to {self.to_time}'

    @property
    def route_number(self):
        return self.route.route_number
    
    @property 
    def bus_number(self):
        return self.bus.bus_number





        

    
    