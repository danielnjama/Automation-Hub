from django.shortcuts import render,get_object_or_404,redirect
from . models import items
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from datetime import datetime
from django.db.models  import Q

# Create your views here.


def home(request):
    today = datetime. now()
    allitems=items.objects.filter(types__contains='gates')
    gates = items.objects.all()
    return render(request,'index-home.html',{'allitems':allitems,'today':today,"gates":gates})

def contact(request):
    today = datetime. now()
    return render(request,'contacts.html',{'today':today})

def swinging_gates(request):
    today = datetime. now()
    gates = items.objects.filter(types='swinging-gates')
    types= "Swinging Gates"
    title=types
    return render(request,'gates.html',{"today":today,"gates":gates,"types":types,"title":title})

def garage_gates(request):
    today = datetime. now()
    gates = items.objects.filter(types='garage-gates')
    types= "Garage Gates"
    title=types
    return render(request,'gates.html',{"today":today,"gates":gates,"types":types,"title":title})


def sliding_gates(request):
    today = datetime. now()
    gates = items.objects.filter(types='sliding-gates')
    types= "Sliding Gates"
    title=types
    return render(request,'gates.html',{"today":today,"gates":gates,"types":types,"title":title})




def aboutus(request):
    today = datetime. now()
    allitems=items.objects.filter(types__contains='gates')
    return render(request,'index.html',{'today':today,"allitems":allitems})



def cctv(request):
    today = datetime. now()
    gates = items.objects.filter(Q(types='Flood-Lights') | Q(types="CCTV"))
    types="CCTV and Flood Lights"
    title=types
    return render(request,'gates.html',{"today":today,"gates":gates,"types":types,"title":title})


def gallery(request):
    today = datetime. now()
    allitems=items.objects.all()
    return render(request,'gallery.html',{'allitems':allitems,'today':today})



def send_email(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    
    if name and email and subject and message:
        message = ('Name: {} \n Email: {} \n Message: {}'.format(name,email,message))
        to_email=settings.EMAIL_HOST_USER
        try:
            send_mail(subject, message, email, [to_email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        message='Thank you {} for contacting us. we\'ll get back to you shortly'.format(name)
        today = datetime. now()
        return render(request,'message.html',{'message':message,'today':today})
        #messages.success(request,'Thank you for contacting us. we\'ll get back to you shortly \n <a href="https://hitechcomputers.herokuapp.com/">Go Back Home </a>')
    else:
        
        return HttpResponse('Make sure all fields are entered and valid.')
    
def item_detail(request,types,slug):
    item = get_object_or_404(items,slug=slug)
    types = item.types
    whatsapp_message ="Hi, Im interested with the "+ item.types + " named: " + item.title + " posted on your website: How much will it cost ?"
    message = whatsapp_message.replace(" ","%20")
    return render(request,'single.html',{'item':item,"message":message})

