from django.db import models
import pandas as pd
# Create your models here.
df = pd.read_csv('/home/apprenant/Téléchargements/Loan_project/data.csv')
indus = df.Industry.unique()
class Features(models.Model):

    industries = [(i,i) for i in indus]
    yesno = [('Oui','Oui'),('Non','Non')]
    urbral = [('Urbain','Urbain'),('Rural','Rural')]

    Industry = models.CharField(max_length=80,choices=industries,default=industries[0])
    Term = models.PositiveIntegerField(null=False,default=12)
    NoEmp = models.PositiveIntegerField(null=False,default=5)
    GrAppv = models.FloatField(null=False,default=10000.0)
    NewExist = models.CharField(max_length=9,default='1')
    CreateJob = models.PositiveIntegerField(null=False,default=0)
    RetainedJob = models.PositiveIntegerField(null=False,default=0)
    FranchiseCode= models.CharField(max_length= 90,null=False,default='1')
    UrbanRural = models.CharField(max_length=9,default='0')
    Real_estate = models.CharField(max_length=9,default='0')
