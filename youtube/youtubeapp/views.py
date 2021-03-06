langue=['af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ceb',
'zh-CN' ,'zh-TW' ,'co','hr','cs','da','nl','eo','et','fi','fr'
,'fy','gl','ka','de','el','gu','ht','ha','haw ','he' ,'hi','hmn',
'hu','is','ig','id','ga','it','ja','jv','kn','kk','km','rw','ko','ku','ky','lo','la','lv','lt',
'lb','mk','mg','ms','ml','mt','mi','mr','mn','my','ne','no','ny','or','ps','fa','pl','pt','pa',
'ro','ru','sm','gd','sr','st','sn','sd','si','sk','sl','so'
,'es','su','sw','sv','tl','tg','ta','tt','te','th','tr','tk','uk','ur','ug','uz','vi','cy','xh',
'yi','yo','zu','ca','en']


from django.urls import reverse
from django.http import  Http404
import pytube
from pytube import YouTube
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import Utilisateur
from django.contrib.auth import authenticate, login
from django.contrib import messages
import os

from django.http import JsonResponse
from django.shortcuts import render, redirect
import json

from youtubeapp.forms import EntryCreationForm
from youtubeapp.models import Entry, Language
from youtubeapp.forms import contactformemail
from django.core.mail import send_mail

# Create your views here.
"""def index(request):
    Lang = Language.objects.all()
    return render(request, 'index.html', {"Language" : Lang})"""


def about(request):
    return render(request, 'about.html')


def first(request):
    form = EntryCreationForm(instance=Entry.objects.first())
    if request.is_ajax():
        term = request.GET.get('term')
        #e=request.POST.getlist('perc')
        #print(lngue[e])
        #print(lngue[e])
        languages = Language.objects.all().filter(title__icontains=term)
        response_content = list(languages.values())
        return JsonResponse(response_content, safe=False)
    if request.method == 'POST':
        form = EntryCreationForm(request.POST, instance=Entry.objects.first())
        if form.is_valid():
            # print(request.POST)
            for key, val in request.POST.items():
                if key == 'language':
                    #print(val)
                    form.save()
            return redirect('first')
    form2 = Utilisateur()
    if request.method == 'POST':
        form2 = Utilisateur(request.POST)
        if form2.is_valid():
            form2.save()
            user = form2.cleaned_data.get('username')
            messages.success(request, 'account Successfully create for ' + user+ ',  login now')
            return redirect('first')
        else:
            messages.error(request, 'Some error in your informations, Try again!!!')
    context = {'form2': form2}

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        #print(password)
        user=authenticate(request, username=username,password= password)
        if user is not None:
            login(request, user)
            #
                #return redirect('name')
            #else:
                #return redirect('n')
            return redirect('name')

        else:
            messages.error(request, "Some error in Username and/or Password")
    return render(request, 'first.html',{'form': form, 'form2': form2 })

"""
def fru(request):subscr_failed subscr_cancel
     if subscr_signup in IPN:
         if dtetime 
         redirect('home')
     if subscr_eot in IPN:
         redirect('name')"""

def own(request):
    return render(request,'own.html' )
def online(request):
    return render(request,'online.html' )

def languages(request):
    return render(request,'n.html')

def error(request):
    return render(request,'error.html' )

def index(request):
    form=EntryCreationForm(instance= Entry.objects.first())
    if request.is_ajax():
        term=  request.GET.get('term')
        #z = request.POST.getlist('pecr')
       # print(z)
        #langue[]
        #print()
        # print(request.GET.get('_type'))
        languages= Language.objects.all().filter(title__icontains= term)
        response_content = list(languages.values())
        return JsonResponse(response_content, safe=False)
    if request.method == 'POST':
        form = EntryCreationForm(request.POST, instance=Entry.objects.first())
        if form.is_valid():
            #print(request.POST)
            for key, val in request.POST.items():
                if key == 'language':
                    e=int(val)
                    print(e)
                    print(langue[e])
                    form.save()

            return redirect('home')
    form1 = contactformemail()
    if request.method=='POST':
        form1 = contactformemail(request.POST)
        if form1.is_valid():
            frommail = form1.cleaned_data['Email']
            subject = form1.cleaned_data['subject']
            message = form1.cleaned_data['message']
            send_mail(subject, message, frommail, ['sekokou27@gmail.com', frommail])
            return redirect('home')
            messages.success(request, "Your message is  send!")
        else:
            messages.error(request, "Some error is detected, please try again")
    return render(request,'index.html',{'form': form, 'form1':form1})


def download(request):
    global url
    if request.method=='POST':
        form = EntryCreationForm(request.POST, instance=Entry.objects.first())
        url = request.POST.get('url')
        yt = YouTube(url)
        video = []
        # language = request.GET.get('language')
        video = yt.streams.filter(progressive=True).all()
        embed_link = url.replace("watch?v=", "embed/")
        Title = yt.title
        context = {'video': video, 'embed': embed_link, 'title': Title}
        if form.is_valid():
            #print(request.POST)
            for key, val in request.POST.items():
                if key == 'language':
                    e = int(val)
                    print(e)
                    print(langue[e])
                    #form.save()
    # print(language)
    return render(request, 'download.html',context )



def yt_download_done(request,resolution):
    global url
    homedir = os.path.expanduser("~")
    dirs=homedir+ '/Downloads'
    if request.method == "POST":
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        #yt.download('/path/to/download/directory')
        return  render(request, 'done.html')
    else:
        return render(request, 'error.html')


"""from django.shortcuts import redirect

def list_articles(request, year,month):

# Il veut des articles ? Soyons fourbe et redirigeons le vers djangoproject.com 5
     return redirect("https://www.djangoproject.com")"""










"""def acces(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(password)
        user=authenticate(request, username=username,password= password)
        if user is not None:
            login(request, user)
            return redirect('name')
        else:
            messages.info(request, "Some error in Username and/or Password")
    return render(request, 'first.html', { })"""




def error(request):
    return render(request,'error.html' )
def done(request):
    return render(request,'done.html' )




from .forms import  SubscriptionForm

def subscription(request):
    if request.method == 'POST':
        f = SubscriptionForm(request.POST)
        if f.is_valid():
            request.session['subscription_plan'] = request.POST.get('plans')
            return redirect('process_subscription')
    else:
        f = SubscriptionForm()
    return render(request, 'n.html', locals())


#...



def process_subscription(request):

    subscription_plan = request.session.get('subscription_plan')
    host = request.get_host()

    if subscription_plan == '1-Day subscription':
        price = "1"
        billing_cycle = 1
        billing_cycle_unit = "D"
    elif subscription_plan == '1-Month subscription':
        price = "10"
        billing_cycle = 1
        billing_cycle_unit = "M"


    paypal_dict  = {
        "cmd": "_xclick-subscriptions",
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        "a3": price,  # monthly price
        "p3": billing_cycle,  # duration of each unit (depends on unit)
        "t3": billing_cycle_unit,  # duration unit ("M for Month")

        "src": "1",  # make payments recur
        "sra": "1",  # reattempt payment on payment error
        "no_note": "1",  # remove extra notes (optional)
        'item_name': 'Content subscription',
        'custom': 1,     # custom data, pass something meaningful here
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('home')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('first')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")
    return render(request, 'process_subscription.html', locals())


#...
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from datetime import datetime, timedelta






@receiver(valid_ipn_received)
def ipn_receiver(sender, **kwargs):
    ipn_obj = sender

    # check for Buy Now IPN
    if ipn_obj.txn_type == 'web_accept':

        if ipn_obj.payment_status == ST_PP_COMPLETED:
            # payment was successful
            print('great!')
            order = get_object_or_404(Order, id=ipn_obj.invoice)

            if order.get_total_cost() == ipn_obj.mc_gross:
                # mark the order as paid
                order.paid = True
                order.save()

    # check for subscription signup IPN
    elif ipn_obj.txn_type == "subscr_signup":

        # get user id and activate the account
        id = ipn_obj.custom
        user = User.objects.get(id=id)
        user.active = True
        o = datetime.now()
        final = o + timedelta(days=30, hours=0,
                              minutes=00)
        redirect("home")

        user.save()

        subject = 'Sign Up Complete'

        message = 'TransLoder thanks you for subscribing to its services !'

        email = EmailMessage(subject,
                             message,
                             'TransLoder@gmail.com',
                             [user.email])

        email.send()

    # vérifier le paiement de l'abonnement IPN
    elif ipn_obj.txn_type == "subscr_payment":

        # obtenir l'ID utilisateur et prolonger l'abonnement
        id = ipn_obj.custom
        user = User.objects.get(id=id)
        # user.extend()  # étendre l souscription

        subject = 'Your Invoice for {} is available'.format(
            datetime.strftime(datetime.now(), "%b %Y"))

        message = 'Thanks for using our service. The balance was automatically ' \
                  'charged to your credit card.'

        email = EmailMessage(subject,
                             message,
                             'TransLoder@gmail.com',
                             [user.email])

        email.send()

    # vérifier si le paiement d'abonnement a échoué IPN
    elif ipn_obj.txn_type == "subscr_failed":
        pass

    # check for subscription cancellation IPN
    elif ipn_obj.txn_type == "subscr_cancel":
        pass
    """if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        #print(password)
        user=authenticate(request, username=username,password= password)
        if user is not None:
            login(request, user)
            if ipn_obj.txn_type == "subscr_eot":
                if datetime.now() > final:
                    
                    return redirect("name")
                    subject = 'Account expired'

                    message = 'Dear user, your account on TransLoder is expired ' \
                      'Subscribe now for begin new section.'

                    email = EmailMessage(subject,
                                 message,
                                 'TransLoder@gmail.com',
                                 [user.email])

                    email.send()
            else: 
                return redirect("home")

return render(request, 'first.html')"""



from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
#from .models import Product, Order, LineItem
#from .forms import CartForm, CheckoutForm

#...
"""
def checkout(request):
    #...

def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.total_cost().quantize(
            Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'index.html', {'order': order, 'form': form})

from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Order, LineItem
#...


def process_payment(request):
    #...


@csrf_exempt
def payment_done(request):
    return render(request, 'ecommerce_app/payment_done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'ecommerce_app/payment_cancelled.html')


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
        #...
        #...

            cart.clear(request)

            request.session['order_id'] = o.id
            return redirect('process_payment')


    else:
        form = CheckoutForm()
        return render(request, 'ecommerce_app/checkout.html', locals())
        """