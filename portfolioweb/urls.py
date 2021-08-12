from django.urls import path
from .views import index,contactme,aboutme
app_name='portfolioweb'

urlpatterns=[
    path('',index,name='index_url'),
    path('contact/',contactme,name='contact_url'),
    path('about/',aboutme,name="about"),
]