from django.db import models

# Create your models here.

class Airport(models.Model):

    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):

    origin = models.ForeignKey( Airport, on_delete=models.CASCADE, related_name="departures" )
    destination = models.ForeignKey( Airport, on_delete=models.CASCADE, related_name="arrivals" )
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: from {self.origin} to {self.destination} for {self.duration} minutes"
    

class Passenger(models.Model):

    first = models.CharField( max_length=64 )
    last = models.CharField( max_length=64 )
    # The blank identifier helps us to allow users to have no flights assigned to them
    # The related_name identifier allows us to reverse access the users assigned to a certain flight
    flights = models.ManyToManyField( Flight, blank=True, related_name="passengers" )

    # For aesthetics
    def __str__(self) -> str:
        return f"{self.first} {self.last}"
    
