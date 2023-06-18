from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path(route='', view=views.feed, name='feed'),
    path(route='upload/', view=views.upload_file, name='upload'),
    path(route='download/<int:file_id>/', view=views.download_file_view, name='download'),
    path(route='email-file/<int:file_id>/', view=views.email_file_view, name='email_file')
]
