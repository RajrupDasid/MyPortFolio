from django.db import models
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    email=models.EmailField(max_length=255)
    contact=models.CharField(max_length=20)
    bio=RichTextUploadingField()
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
    #portfolio_image=models.ImageField(upload_to='Portfolio_images')
    description=RichTextUploadingField()
    #string representation

    def __str__(self):
        return f"{self.title}"

class MyPortFolio(models.Model):
    #careersummary=models.TextField(default="Write down career summary")
    careersummary=RichTextUploadingField()
    biography=RichTextUploadingField()
    skills=RichTextUploadingField()

    def __str__(self):
        return f"{self.careersummary}"


class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    description=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.email}"
