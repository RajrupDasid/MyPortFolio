from django.shortcuts import render,redirect
from .models import Details,PortFolio,MyPortFolio,Contact,PageImage,Service,DetailedPortFolio
# Create your views here.
def index(request):
    details=Details.objects.all()
    portfolio=PortFolio.objects.all()
    myportfolio=MyPortFolio.objects.all()
    dev="I AM A CERTIFIED PYTHON DEVELOPER"
    greet="HELLO, I AM"
    #contact submission
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        description=request.POST['description']
        contact=Contact(name=name,email=email,phone=phone,description=description)
        contact.save()
    #contact submission ends
    context={
        'details':details,
        'pf':portfolio,
        'my':myportfolio,
        'dev':dev,
        'greet':greet,
    }
    return render(request,'portfolioweb/index.html', context)

def contactme(request):
    bg=PageImage.objects.all()
    print(bg)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        description=request.POST['description']
        contact=Contact(name=name,email=email,phone=phone,description=description)
        contact.save()
    context={
        'bg':bg,
    }
    return render(request,'portfolioweb/contact.html',context)

def aboutme(request):
    about=Details.objects.all()
    context={
        'about':about,
    }
    return render(request,'portfolioweb/aboutme.html',context)


def myservices(request):
    services=Service.objects.all()
    context={
        'services':services,
    }
    return render(request,'portfolioweb/services.html',context)


def myportfolio(request):
    myportfolio=DetailedPortFolio.objects.all()

    context={
        "mpf":myportfolio,
    }
    return render(request,'portfolioweb/myportfolio.html',context)

def home(request):
    details=Details.objects.all()
    portfolio=PortFolio.objects.all()
    myportfolio=MyPortFolio.objects.all()
    dev="I AM A CERTIFIED PYTHON DEVELOPER"
    greet="HELLO, I AM"
    #contact submission
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        description=request.POST['description']
        contact=Contact(name=name,email=email,phone=phone,description=description)
        contact.save()
    #contact submission ends
    context={
        'details':details,
        'pf':portfolio,
        'my':myportfolio,
        'dev':dev,
        'greet':greet,
    }
    return render(request,'portfolioweb/index.html', context)

