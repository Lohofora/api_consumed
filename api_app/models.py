from django.db import models

# Create your models here.
class ApiModel(models.Model):
    slug = models.CharField(
        null=True, #la valeur peut être nulle dans la BDD
        blank = False, #pour rendre obligatoire la case
        max_length=100)
    convert = models.CharField(
        null=False, 
        blank = False,
        max_length=100)