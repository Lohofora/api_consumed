from django import forms
from . import models #le "." signifie la base, "models" permet de lier cette page a models.py

class ApiForm(forms.ModelForm):
    class Meta : #permet gérer la mise en forme
        model = models.ApiModel #créé formulaire // info qui sont sur models.py
        fields = "__all__" #dans models.py je veuxque tu reprenne tout
        labels = {
            "slug":"Entez votre cryptomonnaie ici",
            "convert":"Entrez votre devise ici"
        }
