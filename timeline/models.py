from django.db import models
from django.db.models import signals

from geopy.geocoders import GoogleV3 as Geo

class Event(models.Model):
    SINGLE = 'SI'
    SPAN_START = 'SS'
    SPAN_END = 'SE'
    TYPE_CHOICES = (
        (SINGLE, "Single"),
        (SPAN_START, "Span Start"),
        (SPAN_END, "Span End")
    )

    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=SINGLE)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    location = models.TextField(blank=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    other = models.ForeignKey( 'self', blank=True, null=True )

def geocode( sender, instance, **kwargs ):
    if instance.location:
        g = Geo()
        location = g.geocode( instance.location )
        instance.latitude = location.latitude
        instance.longitude = location.longitude

signals.pre_save.connect( geocode, sender=Event )
