from django.shortcuts import render
from . import forms
from requests import Session
import json


def api(request): 
#requete de l'API ici à partir de la documentation du site de l'API
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '95973e4d-9ca4-4f9a-803a-1ed43083754b' #clé du site de l'api
    }

    session = Session()
    session.headers.update(headers)


    if request.method =='POST':
        form = forms.ApiForm(request.POST)
        if form.is_valid():
            response = session.get(url, params=form.cleaned_data) #params de l'API
            print(form.cleaned_data)
            form.save()
            info = json.loads(response.text) #json.loads permet juste de retourner le json sous forme de dictionnaire
            return render(request, 'api_app/reponse_formulaire.html', context = {'form':form, 'info':info})

    else :
        form = forms.ApiForm()
    return render(request, 'api_app/formulaire.html', context = {'form':form})