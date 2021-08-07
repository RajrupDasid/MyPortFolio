from django.shortcuts import render
from .models import Details,PortFolio
# Create your views here.
def index(request):
    details=Details.objects.all()
    portfolio=PortFolio.objects.all()
    context={
        'details':details,
        'pf':portfolio,
    }
    return render(request,'portfolioweb/index.html', context)