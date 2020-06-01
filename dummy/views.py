  
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import datetime
from .models import *
from django.db.models import Count
from django.utils import timezone
def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             user = form.save()
             login(request, user)
             #  log the user in
             return redirect('dummy:logged')
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.date()
        Create_visit=LandingPageVisitor.objects.create(visit_date=current_date,visit_time=current_time)
        form = UserCreationForm()
    return render(request, 'dummy/signup.html', { 'form': form })

class Logged(object):
    loggedi = -2

@login_required(login_url="/dummy/login")
def logged(request):
    username=request.user.username
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.date()
    if Logged.loggedi < 0:
        logged = LoggedIn.objects.create(user_name=username,visit_date=current_date,visit_time=current_time)
    Logged.loggedi = 1
    return render(request,'dummy/logged.html')


class Balance(object):
    balance = -2

class Funds(object):
    funds = -2

class Loans(object):
    loans = -2



@login_required(login_url="/dummy/login")
def balance(request):
    username=request.user.username
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.date()
    if Balance.balance < 0:
        balanceChecked= BalanceActivity.objects.create(user_name=username,visit_date=current_date,visit_time=current_time)
    Balance.balance = 1
    return render(request,'dummy/balance.html')

@login_required(login_url="/dummy/login")
def funds(request):
    username=request.user.username
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.date()
    if Funds.funds < 0:
        FundsChecked= FundsActivity.objects.create(user_name=username,visit_date=current_date,visit_time=current_time)
    Funds.funds = 1
    return render(request,'dummy/funds.html')

@login_required(login_url="/dummy/login")
def loan(request):
    username=request.user.username
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.date()
    if Loans.loans < 0:
        LoanChecked=LoanActivity.objects.create(user_name=username,visit_date=current_date,visit_time=current_time)
    Loans.loans = 1
    return render(request,'dummy/loan.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('dummy:logged')
    else:
        form = AuthenticationForm()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.date()
        Create_visit=LoginActivity.objects.create(visit_date=current_date,visit_time=current_time)
    return render(request, 'dummy/login.html', { 'form': form })


def logout_view(request):
    if request.method == 'POST':
            logout(request)
            Balance.balance = -2
            Loans.loans = -2
            Funds.funds = -2
            Logged.loggedi = -2
            return redirect('dummy:logged')


def index(request):
  
    count=LandingPageVisitor.objects.filter().count()
    p=LandingPageVisitor.objects.values('visit_date').annotate(dcount=Count('visit_date'))
    arrX=p.values_list('visit_date',flat=True)
    arrY=p.values_list('dcount',flat=True)
    arrX=list(arrX)
    arrX= [i.strftime("%m/%d/%y") for i in arrX]
    arrY=list(arrY)
    print(arrX)
    print(arrY)
    
    return render(request, "index.html",{"count":count,'arrX':arrX,'arrY':arrY})



def indexLogin(request):
  
    count=LoginActivity.objects.filter().count()
    p=LoginActivity.objects.values('visit_date').annotate(dcount=Count('visit_date'))
    arrX=p.values_list('visit_date',flat=True)
    arrY=p.values_list('dcount',flat=True)
    arrX=list(arrX)
    arrX= [i.strftime("%m/%d/%y") for i in arrX]
    arrY=list(arrY)
    print(arrX)
    print(arrY)
    
    return render(request, "index.html",{"count":count,'arrX':arrX,'arrY':arrY})


def indexLogged(request):
    count=LoggedIn.objects.filter().count()
    p=LoggedIn.objects.values('visit_date').annotate(dcount=Count('visit_date'))
    arrX=p.values_list('visit_date',flat=True)
    arrY=p.values_list('dcount',flat=True)
    arrX=list(arrX)
    arrX= [i.strftime("%m/%d/%y") for i in arrX]
    arrY=list(arrY)
    print(arrX)
    print(arrY)
    
    return render(request, "index.html",{"count":count,'arrX':arrX,'arrY':arrY})


def indexBalance(request):
    count=BalanceActivity.objects.filter().count()
    p=BalanceActivity.objects.values('visit_date').annotate(dcount=Count('visit_date'))
    arrX=p.values_list('visit_date',flat=True)
    arrY=p.values_list('dcount',flat=True)
    arrX=list(arrX)
    arrX= [i.strftime("%m/%d/%y") for i in arrX]
    arrY=list(arrY)
    print(arrX)
    print(arrY)
    
    return render(request, "index.html",{"count":count,'arrX':arrX,'arrY':arrY})


def indexLoans(request):
    count=LoanActivity.objects.filter().count()
    p=LoanActivity.objects.values('visit_date').annotate(dcount=Count('visit_date'))
    arrX=p.values_list('visit_date',flat=True)
    arrY=p.values_list('dcount',flat=True)
    arrX=list(arrX)
    arrX= [i.strftime("%m/%d/%y") for i in arrX]
    arrY=list(arrY)
    print(arrX)
    print(arrY)
    
    return render(request, "index.html",{"count":count,'arrX':arrX,'arrY':arrY})

def indexFunds(request):
    count=FundsActivity.objects.filter().count()
    p=FundsActivity.objects.values('visit_date').annotate(dcount=Count('visit_date'))
    arrX=p.values_list('visit_date',flat=True)
    arrY=p.values_list('dcount',flat=True)
    arrX=list(arrX)
    arrX= [i.strftime("%m/%d/%y") for i in arrX]
    arrY=list(arrY)
    print(arrX)
    print(arrY)
    
    return render(request, "index.html",{"count":count,'arrX':arrX,'arrY':arrY})



    