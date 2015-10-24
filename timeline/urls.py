from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.view, name='view' ),
    url(r'^events$', views.events, name='events' ),
]
