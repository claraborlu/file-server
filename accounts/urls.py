from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
    path(route='signup/', view=views.signup, name='signup'),
    path(route='account-activation-sent/', view=views.account_activation_sent, name='account_activation_sent'),
    path(route='activate/<uidb64>/<token>/', view=views.activate, name='activate'),
    path(route='login/', view=views.login_view, name='login'),
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
]
