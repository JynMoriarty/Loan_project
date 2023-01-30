from django.db import models
import pandas as pd
# Create your models here.
df = pd.read_csv('/home/apprenant/Téléchargements/Loan_project/data.csv')
indus = df.Industry.unique()
state = df.State.unique()

class Features(models.Model):

    industries = [(i,i) for i in indus]
    yesno = [('1','Oui'),('0','Non')]
    urbral = [('0','Non Défini'),('1','Urbain'),('2','Rural')]
    existing = [('0','Existante'),('1','Nouvelle')]
    Industry = models.CharField(max_length=80,choices=industries,default=industries[0])
    Term = models.PositiveIntegerField(null=False,default=12)
    NoEmp = models.PositiveIntegerField(null=False,default=5)
    GrAppv = models.FloatField(null=False,default=10000.0)
    NewExist = models.CharField(max_length=9,choices=existing,default=existing[0])
    CreateJob = models.PositiveIntegerField(null=False,default=0)
    RetainedJob = models.PositiveIntegerField(null=False,default=0)
    FranchiseCode = models.CharField(max_length= 90 ,null=False,default='1')
    UrbanRural = models.CharField(max_length=9,choices=urbral,default=urbral[0])
    Real_estate = models.CharField(max_length=9,choices=yesno,default=yesno[0])

class State(models.Model):
    states = [(i,i) for i in state]

    State = models.CharField(max_length=3,choices =states,default=state[0])
