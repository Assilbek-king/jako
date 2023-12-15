from main.models import *
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def indexHandler(request):
    diagrams = Diagram.objects.all()
    # tovars = Tovar.objects.order_by('status')
    # photos = Photo.objects.all()

    # if request.method == 'POST':
    #     BOT_TOKEN = "6888390474:AAE2OQa2E9Unu_vvOf4ZKnwJC0RXIU_GsQE"
    #     TELEGRAM_CHAT_ID = "604469732"
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     comment = request.POST.get('comment')
    #     feedback = Feedback(name=name, phone=phone, comment=comment)
    #     feedback.save()
    #     if comment:
    #         message = f"Новый клиент\nИмя: {name}\nНомер: {phone}\nТовар: {comment}"
    #     else:
    #         message = f"Новый клиент\nИмя: {name}\nНомер: {phone}"
    #     response = requests.get(
    #         f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")
    #     from django.shortcuts import redirect
    #     return redirect('/')

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

    return render(request, 'site/404.html', {
        'active_user': active_user
    })

def transactionHandler(request):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = UserProfile.objects.get(id=int(user_id))

    return render(request, 'site/404.html', {
        'active_user': active_user
    })