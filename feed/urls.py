from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path(route='feed/', view=views.feed, name='feed'),
]
