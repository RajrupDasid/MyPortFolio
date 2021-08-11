from django.urls import path
from .views import index,contactme
app_name='portfolioweb'

urlpatterns=[
    path('',index,name='index'),
    path('contact/',contactme,name='contact_url'),
]