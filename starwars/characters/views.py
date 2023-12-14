from django.shortcuts import render
import requests
import json

def all(request):
    c_url = "https://swapi.dev/api/people/"
    lista = []
    max_height = 0
    max_mass = 0
    # c_url = character['next']
    while c_url != None:
        c_response = requests.get(c_url)
        character = c_response.json()
        print(c_url)
        for c in character['results']:
            name = c['name']
            height = c['height']
            mass = c['mass']
            world_url = c['homeworld']
            world_number = c['homeworld'].split('/')[-2]
            w_response = requests.get(world_url)
            world = w_response.json()
            world_name = world['name']

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
            lista.append([name, height, mass, world_name, world_number])
        c_url = character['next']
        # c_response = requests.get(c_url)
        # character = c_response.json()
    total = len(lista)
    contexto = {'lista': lista,
                'total': total,
                'max_height': max_height,
                'max_mass': max_mass}
    return render(request,'all.html', contexto)

def inplanet(request):
    world_number = request.GET.get('planet')
    w_url = "https://swapi.dev/api/planets/" + world_number
    w_response = requests.get(w_url)
    world = w_response.json()
    world_name = world['name']
    lista = []
    max_height = 0
    max_mass = 0

    print (world)

    for c_url in world['residents']:
        print(c_url)
        c_response = requests.get(c_url)
        c = c_response.json()
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
        lista.append([name, height, mass, world_name, world_number])

    total = len(lista)
    contexto = {'lista': lista,
                'total': total,
                'max_height': max_height,
                'max_mass': max_mass}
    return render(request,'all.html', contexto)
