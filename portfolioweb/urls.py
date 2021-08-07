from django.urls import path
from .views import index
app_name='portfolioweb'

urlpatterns=[
    path('',index,name='index'),
]