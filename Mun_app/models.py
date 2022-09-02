import email
from email.message import EmailMessage
from tokenize import Name
from turtle import title
from django.db import models
from django.utils.safestring import mark_safe 

#It lists the experiences in the About page.
class Experience(models.Model):
    title =models.CharField(blank=True, null=True,max_length=150)
    experience = models.TextField()
    media = models.ImageField(blank=True, null=True,upload_to ='media')
    def __str__(self):
        return self.title 
        
class Achievement(Experience):
    def __str__(self):
        return self.title 

class Blog(models.Model):
    title =models.CharField(max_length=200, null=True)
    body =models.TextField()
    media =models.ImageField(blank=True, null=True,upload_to ='media')
    dte= models.DateField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.title

 
#Centralize text with pages: only to unite the naming and linking each page with its text
class Web_Pages(models.Model):
    page = models.CharField(max_length=200, default='def')
    def __str__(self):
        return self.page

#This is designed to delete all the text in the frondend template and for east mangment
class TextManagementSystem(models.Model):
    PageAssociated =  models.ForeignKey(Web_Pages, on_delete=models.CASCADE)
    Body= models.TextField(null=True)  
    media= models.ImageField(blank=True, null=True, upload_to ='Muntadher_protfolio/media')
    Purpose= models.CharField(max_length=200, default='def')
    @property
    def thumbnail_preview(self):
        print (self.media.url)
        return mark_safe( '<img src="{}" width="100" height="75" />'.format(self.media.url) )
     


class TvSeries(models.Model):
    SeriesName =  models.CharField(max_length=200, default='The office')
    VentSpace= models.TextField(null=True,  blank=True)  
    media= models.ImageField(blank=True, null=True, upload_to ='media')
    Notes= models.CharField(max_length=200, default='Nothing')
    def __str__(self):
        return self.SeriesName
class Explore(models.Model):
    Name = models.CharField(max_length=255, blank= True, null=True)
    Choose = models.CharField(max_length=255,choices=(("Feedback","Feedback"),("Question","Question")))
    Message = models.CharField(max_length=255)
    def __str__(self):
        x=[self.Name if self.Name else str(self.id) or "Nothing" ]
        return x[0]
        
class Subscribe(models.Model):
    Email= models.EmailField(max_length=254)
    def __str__(self):
        return self.Email

            