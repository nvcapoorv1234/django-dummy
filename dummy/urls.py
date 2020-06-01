from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'dummy'

urlpatterns = [
    
    path('', views.signup_view, name = "signup"),
    path('login', views.login_view, name = "login"),
    path('logout', views.logout_view, name = "logout"),
    path('balance', views.balance, name = "balance"),
    path('funds', views.funds, name = "funds"),
    path('loan', views.loan, name = "loan"),
    path('logged', views.logged, name = "logged"),
    path('monitor', views.index, name = "monitor"),
    
]