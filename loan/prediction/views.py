from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
import requests 

# liste = ['Real_estate','UrbanRural','NewExist','FranchiseCode']

# def transformation(dict,liste):
#     for key,v in dict.items():
#         if key in liste:
#             if v in ['Oui','Urbain','Existante']:
#                 v = 0
#             elif v in ['Non','Rural','Nouvelle']:
#                 v=1
#             else:
#                 v= str(v)
#     return dict
def accueil(request):

    return render(request,'accueil.html')
def home_view(request):
    headers = {'accept' : 'application/json','Content-Type': 'application/json'}
    quest = forms.PredictionForm
    state = forms.StateForm
    if request.method == 'POST':
        form=quest(request.POST or None)
        form2 = state(request.POST or None)
        if form.is_valid() and form2.is_valid():
            url = 'http://127.0.0.1:8001/predict'
            res = form.cleaned_data | form2.cleaned_data
            print(type(form.cleaned_data))
            conversion = json.dumps(res)
            info= requests.post(url = url,data = conversion,headers=headers)
            raw_result = info.text
            print(raw_result)
            print(type(raw_result))
            result = None
            if raw_result == '0':
                result = 'Félicitations votre prêt a été accordé !'
            elif raw_result == '1':
                result = "Malhereusement votre dossier n'a pas été retenu , une prochaine fois peut-être ;)" 

            return render(request,"result.html",{"result":result})
            
    else:


        return render(request, "homepage.html", {'form':quest,'form2':state})

