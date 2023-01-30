from django.urls import path # Import du module Path  
from .views import * # Import de notre fichier views

urlpatterns = [
    path("", accueil, name="home"),
    path("questionnaire/", home_view, name="questionnaire"),
]