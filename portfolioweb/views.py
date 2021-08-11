from django.shortcuts import render
from .models import Details,PortFolio,MyPortFolio,Contact
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