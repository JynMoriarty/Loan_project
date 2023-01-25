from django.shortcuts import render
from . import forms

# Create your views here.

def home_view(request):
    form=forms.PredictionForm
    return render(request, "homepage.html", context={'form':form})