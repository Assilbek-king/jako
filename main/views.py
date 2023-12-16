from main.models import *
import requests
from datetime import datetime, timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def indexHandler(request):
    diagrams = Diagram.objects.all()


    return render(request, 'site/index.html', {
        'diagrams': diagrams,
    })


def loginHandler(request):
    if request.POST:
        email = request.POST.get('email', {})
        password = request.POST.get('password', {})
        if email and password:

            site_user = UserProfile.objects.filter(email=email).filter(password=password)

            if site_user:
                site_user = site_user[0]
                request.session['user_id'] = site_user.id
                return redirect('/cabinet')
            else:
                print('User not found')
        else:
            print('Error arguments')

    return render(request, 'site/page-login.html', {
    })

def logoutHandler(request):
    request.session['user_id'] = None
    return redirect('/')


def kabinetHandler(request):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = UserProfile.objects.get(id=int(user_id))

    return render(request, 'add/index.html', {
        'active_user': active_user
    })

def dohodHandler(request):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = UserProfile.objects.get(id=int(user_id))

    profits = UserProfit.objects.filter(user__id = active_user.id)


    if request.method == 'POST':
        BOT_TOKEN = "6706713973:AAESvl32lMMGKt2Zi9nBow7RK3xWIP1reJg"
        TELEGRAM_CHAT_ID = "604469732"
        withdrawal = request.POST.get('withdrawal')
        userprofit = UserProfit.objects.get(id=int(request.POST.get('userprofit_id', 0)))
        date = datetime.now()
        transaction = UserTransaction(userprofit=userprofit, withdrawal=withdrawal, date=date)
        transaction.save()
        if withdrawal:
            message = f"Инвестор хочет снять деньги \n Имя: {userprofit.user.name} \n Фамилия: {userprofit.user.second_name} \n Номер: {userprofit.user.phone}\n Счет номер: {userprofit.user.card_number}\n Запрос для снятия : {withdrawal}"
        print(f"Инвестор хочет вернуть деньги \n Имя: {userprofit.user.name} \n Фамилия: {userprofit.user.name} \n Номер: {userprofit.user.phone}\n Счет номер: {userprofit.user.card_number}\n Запрос для снятия : ${withdrawal}")
        response = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")
        from django.shortcuts import redirect
        return redirect('/profit')

    return render(request, 'add/transactions.html', {
        'active_user': active_user,
        'profits': profits,

    })

def transactionHandler(request):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = UserProfile.objects.get(id=int(user_id))

    transactions = UserTransaction.objects.filter(userprofit__user__id = active_user.id, status=True)

    return render(request, 'add/referrals.html', {
        'active_user': active_user,
        'transactions': transactions,
    })