from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# New guys say hi
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect( reverse("login") )
    return render( request, "users/index.html" )


def login_view( request ):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate( request, username=username, password=password )

        if not user:
            return render( request, "users/login.html", {
                "message": "invalid credentials"
            } )
        
        login( request, user )
        return HttpResponseRedirect( reverse( "users:index" ) )
    return render( request, "users/login.html" ) 


def logout_view( request ):
    logout( request )
    return render( request, "users/login.html", {
        "message": "Logged out",
    } )

