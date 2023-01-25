from django.db import models

# Create your models here.

class Features(models.Model):

    industries = [('1','Retail trade'), ('2','Accommodation and food services'),('3','Health care and social assistance'), ('4','Others'), ('5','Manufacturing'),('6','Other services (except public administration) 92 Public administration'),('7','Construction'), ('8','Wholesale trade'), ('9','Educational services'),('10','Real estate and rental and leasing'),('11','Professional, scientific, and technical services'),('12','Information'),('13','Arts, entertainment, and recreation'), ('14','Finance and insurance'),('15','Mining, quarrying, and oil and gas extraction'),('16','Administrative and support and wase management and remediation services'),('17','Transportation and warehousing'),('18','Agriculture, forestry, fishing and hunting'), ('19','Utilities'),('21','Management of companies and enterprises')]
    Industry = models.CharField(max_length=9,choices=industries,default=1)
    Term = models.PositiveIntegerField(null=False,default=12)
    NoEmp = models.PositiveIntegerField(null=False,default=5)
    GrAppv = models.PositiveIntegerField(null=False,default=10000)
    yesno = [('0','Oui'),('1','Non')]
    NewExist = models.CharField(max_length=9,choices=yesno,default=1)
    CreateJob = models.PositiveIntegerField(null=False,default=0)
    RetainedJob = models.PositiveIntegerField(null=False,default=1)
    FranchiseCode= models.PositiveIntegerField(null=False,default=1)
    urbral = [('1','Urbain'),('2','Rural')]
    UrbanRural = models.CharField(max_length=9,choices=urbral,default=1)
    Real_estate = models.CharField(max_length=9,choices=yesno,default=1)
