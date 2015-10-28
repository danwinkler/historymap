import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from .models import Event

def view( request ):
    return render( request, 'timeline/view.html' )

def events( request ):
    return HttpResponse( serializers.serialize("json", Event.objects.all() ) )
