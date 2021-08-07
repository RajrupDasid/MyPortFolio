from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    email=models.EmailField(max_length=255)
    contact=models.CharField(max_length=20)
    bio=models.TextField()
    address=models.TextField()
    profile_image=models.ImageField(upload_to='profile_image')
    background=models.ImageField(upload_to='background', blank =True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
   
    #string representation
   
    def __str__(self):
        return f"{self.name}"

class PortFolio(models.Model):
    title=models.CharField(max_length=50)
    portfolio_image=models.ImageField(upload_to='Portfolio_images')
    
    #string representation

    def __str__(self):
        return f"{self.title}"
