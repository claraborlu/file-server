from django.urls import path
import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account-activation-sent/', views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login/', views.login_view, name='login'),
]
