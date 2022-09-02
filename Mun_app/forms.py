from django import forms
from .models import *

class FeedbackForm(forms.Form):
    choices=[("Feedback","Feedback"),("Question","Question")]
    type = forms.CharField(max_length=255,widget=forms.Select(choices=choices))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'sky is your limit', 'style': 'width: 600px;', 'class': 'form-control'}))
    sender = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'placeholder': 'Drop your name if you wish', 'style': 'width: 300px;', 'class': 'form-control'}))

class SubscribeForm(forms.Form):
    email = forms.EmailField()
