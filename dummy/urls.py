from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'dummy'

urlpatterns = [
    
    path('', views.signup_view, name = "signup"),
    path('login', views.login_view, name = "login"),
    path('dummy/login', views.login_view, name = "login"),
    path('logout', views.logout_view, name = "logout"),
    path('dummy/out', views.out_view, name = "out"),
    path('balance', views.balance, name = "balance"),
    path('funds', views.funds, name = "funds"),
    path('loan', views.loan, name = "loan"),
    path('logged', views.logged, name = "logged"),
    path('monitor', views.index, name = "monitor"),
    path('monitorLogin', views.indexLogin, name = "monitorLogin"),
    path('monitorUsersLogged',views.indexLogged,name="monitorUsersLogged"),
    path('monitorFunds',views.indexFunds,name="monitorFunds"),
    path('monitorBalance',views.indexBalance,name="monitorBalance"),
    path('monitorLoans',views.indexLoans,name="monitorLoans"),
    path('mainFunction',views.mainFunction,name="mainFunction"),
    path('mainFunction2',views.mainFunction2,name="mainFunction2"),
    
]