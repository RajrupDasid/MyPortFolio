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
    description=models.TextField(default="Wrire the description of the programming language")
    #string representation

    def __str__(self):
        return f"{self.title}"

class MyPortFolio(models.Model):
    careersummary=models.TextField(default="Write down career summary")
    biography=models.CharField(max_length=1000,default='Wirite down biography')
    skills=models.TextField(default="write down skills")

    def __str__(self):
        return f"{self.careersummary}"