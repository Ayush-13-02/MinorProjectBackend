from django.db import models

# Create your models here.
class WaterParameters(models.Model):
    pH = models.FloatField()
    Hardness = models.FloatField()
    Solids = models.FloatField()
    Chloramines = models.FloatField()
    Sulfate = models.FloatField()
    Conductivity = models.FloatField()
    Organic_carbon = models.FloatField()
    Trihalomethanes = models.FloatField()
    Turbidity = models.FloatField()
