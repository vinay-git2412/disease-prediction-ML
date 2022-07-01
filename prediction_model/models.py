from django.db import models

# Create your models here.
class diseasePrediction(models.Model):
    Symptom1 = models.CharField(max_length=20)
    Symptom2 = models.CharField(max_length=20)
    Symptom3 = models.CharField(max_length=20)
    Symptom4 = models.CharField(max_length=20)
    Symptom5 = models.CharField(max_length=20)
    Symptom6 = models.CharField(max_length=20)
    classification = models.CharField(max_length=20)
    
    
class DesandPrec(models.Model):
    Description = models.TextField(max_length=300)
    Precaution_1 =  models.TextField(max_length=300)
    Precaution_2 =  models.TextField(max_length=300)
    Precaution_3 =  models.TextField(max_length=300)
    Precaution_4 =  models.TextField(max_length=300)
    classification = models.CharField(max_length=20)