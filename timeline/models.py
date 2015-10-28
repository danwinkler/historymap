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
    month = models.IntegerField(default=1)
    day = models.IntegerField(default=1)
    name = models.TextField()
    description = models.TextField(blank=True)
    location = models.TextField(blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    other = models.ForeignKey( 'self', blank=True, null=True )

    def __unicode__(self):
        return self.name

def geocode( sender, instance, **kwargs ):
    if instance.location:
        g = Geo()
        location = g.geocode( instance.location )
        instance.latitude = location.latitude
        instance.longitude = location.longitude

signals.pre_save.connect( geocode, sender=Event )
