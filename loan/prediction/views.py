from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
import requests 


        

def home_view(request):
    headers = {'accept' : 'application/json','Content-Type': 'application/json'}
    quest = forms.PredictionForm
    if request.method == 'POST':
        form=quest(request.POST or None)
        if form.is_valid():
            url = 'http://127.0.0.1:8001/predict'
            conversion = json.dumps(form.cleaned_data)
            info= requests.post(url = url,data = conversion,headers=headers)
            result = info.text
            

            return render(request,"result.html",{"result":result})
    else:


        return render(request, "homepage.html", {'form':quest})

