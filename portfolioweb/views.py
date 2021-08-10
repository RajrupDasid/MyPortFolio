from django.shortcuts import render
from .models import Details,PortFolio,MyPortFolio
# Create your views here.
def index(request):
    details=Details.objects.all()
    portfolio=PortFolio.objects.all()
    myportfolio=MyPortFolio.objects.all()
    context={
        'details':details,
        'pf':portfolio,
        'my':myportfolio,
    }
    return render(request,'portfolioweb/index.html', context)