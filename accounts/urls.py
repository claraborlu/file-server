from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path(route='signup/', view=views.signup, name='signup'),
    path(route='activate/<uidb64>/<token>/', view=views.activate, name='activate'),
    path(route='login/', view=views.login_view, name='login'),
    path(route='logout/', view=views.logout_view, name='logout'),
]
