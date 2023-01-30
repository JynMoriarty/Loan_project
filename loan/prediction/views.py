from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
import requests 
import folium
import pandas as pd 
import geopandas as gpd

df = pd.read_csv('/home/apprenant/Bureau/loan/Loan_project/data.csv')

def percent_of_CHGOFF(df):
    nb_CHGOFF = df[df=='1'].shape[0]
    nb_total = df.shape[0]
    return round((nb_CHGOFF / nb_total)*100,2)
df_state = df[['State','MIS_Status']]
df_state = df_state.groupby('State').agg(percent_of_CHGOFF).rename(columns={'MIS_Status' : 'percent_of_CHGOFF'}).reset_index()

gdf = gpd.read_file('/home/apprenant/Bureau/loan/Loan_project/us-states.json')


# read a GeoJSON file with Pandas

# # merge the data and the GeoJSON file
merged = gdf.merge(df_state, left_on='id', right_on='State')

# create a choropleth map
m = folium.Map(location=[50, -95], zoom_start=3)
folium.Choropleth(
geo_data=merged,
name='choropleth',
data=df_state,
columns=['State', 'percent_of_CHGOFF'],
key_on='feature.properties.id',
fill_color='Reds',
fill_opacity=1,
line_opacity=0.4,
legend_name='pourcentage de non remboursement'
).add_to(m)
# ajouter des marqueurs pour chaque état
for row in merged.itertuples():
    if row.percent_of_CHGOFF > 21 :
        folium.Marker(location=[row.geometry.centroid.y, row.geometry.centroid.x], popup=row.name).add_to(m)

folium.LayerControl().add_to(m)
map = m._repr_html_()

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
            print(form2.cleaned_data)
            res = form.cleaned_data | form2.cleaned_data
            print(form.cleaned_data)
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


        return render(request, "homepage.html", {'form':quest,'form2':state,'map': map})

