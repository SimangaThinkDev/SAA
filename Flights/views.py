from django.shortcuts import render
from .models import Flight
# Create your views here.

def index(request):
    return render( request, "Flights/index.html", {
        "flights": Flight.objects.all(),
    } )


def flight( request, flight_id ):
    """Gets the flight by flight ID"""
    print("This happpened")
    requested_flight = Flight.objects.get( pk=flight_id )
    return render( request, "Flights/flight.html", {
        "flight": requested_flight
    } )

