from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home_view(request):
    quest = forms.PredictionForm
    if request.method == 'POST':
        form=quest(request.POST)
        if form.is_valid():
            request.session['result']= form.cleaned_data
            
            return HttpResponseRedirect(reverse(result_view))
    else:

        return render(request, "homepage.html", {'form':quest})

def result_view(request):
    result = request.session.get("result")
    return render(request,"result.html",{"result":result})