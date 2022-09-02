from ssl import Purpose
from tkinter.tix import Form
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from .forms import *
from django.db.models.aggregates import Count
from django.core.mail import send_mail
from PIL import Image
from django.contrib import messages
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'textmanagementsystem_list.html'
    context_object_name= "Highlights"
    def get_queryset(self):
        """Return the last five published questions."""
        return TextManagementSystem.objects.filter(~Q(Purpose ="def"))

def Index(request):
    #Bug, this brngs only the purpose who has not def as a purpose. PO stands for Picture Only
    Highlights = TextManagementSystem.objects.filter(~Q(Purpose ="def"))
    Highlights ={'Highlights':Highlights}  
    return render(request,"index.html", Highlights)

def Previous_experience(request):
    experience = Experience.objects.all()
    experience={"experience":experience}
    print (experience)
    return render(request,"previous_experience.html", experience)
     
#it has subscribe form for eail updates
def Blogf(request):
    #blog_dic = {"blog_dic":Blog.objects.all()}
    form= SubscribeForm()
    blog_dic = Blog.objects.all()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            exploredb = Subscribe(Email=data['email'])
            exploredb.save()
            emails_s_list= Subscribe.objects.all().last()
            print (data['email'])
            send_mail(Blog.objects.all().last().title,Blog.objects.all().last().body,'123muntadher97@gmail.com',[data['email']],fail_silently=False)
            messages.add_message(request, messages.SUCCESS, 'Subsribed!!')
            return render(request,"blog.html", {"blog_dic":blog_dic})
    return render(request,"blog.html", {"form":form, "blog_dic":blog_dic})

def Exploref(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            exploredb = Explore(Name=data['sender'],Choose= data['type'],Message=data['message'])
            exploredb.save()
            send_mail(data['type'],data['message'],data['sender'],["123Muntadher97@gmail.com"])
            form = FeedbackForm()
            return render(request,"explore.html",{"form":form})
    else:
        form = FeedbackForm()
        exploreData= Explore.objects.order_by("?").first()
        print(exploreData)
    return render(request,"explore.html", {"form":form,"exploreData":exploreData})

def TvSeriesf(request):
    Series = TvSeries.objects.all()
    Series={"Series":Series}
    return render(request,"TvSeries.html",Series)

def About(request):
    exp = Experience.objects.get(pk=1)
    exp ={"exp":exp}
    return render(request,"about.html")

     
def Single(request,id):
    achievement= {"achievement":get_object_or_404(Blog, pk=id)}
    print (achievement)
    return render(request, 'single.html',achievement)