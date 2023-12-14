from django.shortcuts import render
import requests
import json

def all(request):
    url = "https://swapi.dev/api/people/"
    lista = []
    max_height = 0
    max_mass = 0
    response = requests.get(url)
    r = response.json()
    while r['next'] != None:
        print(url)
        for c in r['results']:
            name = c['name']
            height = c['height']
            mass = c['mass']
            try:
                height = float(height.replace(',', '.'))
                max_height = height if height > max_height else max_height
            except:
                pass
            try:
                mass = float(mass.replace(',', '.').replace('.', ''))
                max_mass = mass if mass > max_mass else max_mass
            except:
                pass
            lista.append([name, height, mass])
        url = r['next']
        response = requests.get(url)
        r = response.json()
    total = len(lista)
    contexto = {'lista': lista,
                'total': total,
                'max_height': max_height,
                'max_mass': max_mass}
    return render(request,'all.html', contexto)

# Create your views here.
