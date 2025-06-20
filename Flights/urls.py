
from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path( 'flights', views.index, name='index' ),
    path( 'flights/<int:flight_id>', views.flight, name="flight" ),
]
