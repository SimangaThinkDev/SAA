from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger


# Create your views here.

def index(request):
    return render( request, "Flights/index.html", {
        "flights": Flight.objects.all(),
    } )


def flight( request, flight_id ):
    """Gets the flight by flight ID"""
    print("This happpened")
    requested_flight = Flight.objects.get( pk=flight_id )
    passengers = requested_flight.passengers.all()
    return render( request, "Flights/flight.html", {
        "flight": requested_flight,
        "passengers": passengers,
        "non_passengers": Passenger.objects.exclude( flights=requested_flight ).all()
    } )


def book( request, flight_id ):

    if request.method == "POST":

        # Get the flight
        flight = Flight.objects.get( pk=flight_id )

        # Get the passenger by id
        passenger = Passenger.objects.get( pk = int(request.POST["passenger"]) )
        passenger.flights.add( flight )
        print("Right here")

        return HttpResponseRedirect( reverse( "flights:flight", args=(flight.id,) ) )
