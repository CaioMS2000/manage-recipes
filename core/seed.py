from os import system
import json
from .models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato

def delete_all():
    Categoria.objects.all().delete()
    Cozinheiro.objects.all().delete()
    Degustador.objects.all().delete()
    Editor.objects.all().delete()
    Livro.objects.all().delete()
    Ingrediente.objects.all().delete()
    Receita.objects.all().delete()
    Restaurante.objects.all().delete()
    Porcao.objects.all().delete()
    Contrato.objects.all().delete()

def delete_all_users():
    Cozinheiro.objects.all().delete()
    Degustador.objects.all().delete()
    Editor.objects.all().delete()

def create_categories(data):
    for c in data:
        new_category = Categoria.objects.create(name= c['name'], description= c['description'])

def create_users(data):
    chefs = data[0:2]
    tasters = data[2:4]
    editors = data[4:6]

    for chef in chefs:
        Cozinheiro.objects.create(salary= 1, name= chef['first_name'] + ' ' + chef['last_name'], cpf= chef['cpf'], email= chef['email'])

    for taster in tasters:
        Degustador.objects.create(salary= 1, name= taster['first_name'] + ' ' + taster['last_name'], cpf= taster['cpf'], email= taster['email'])

    for editor in editors:
        Editor.objects.create(salary= 1, name= editor['first_name'] + ' ' + editor['last_name'], cpf= editor['cpf'], email= editor['email'])

def create_ingredients(data):
    for ingredient in data:
        new_ingredient = Ingrediente.objects.create(name=ingredient['name'], description=ingredient['description'])

def create_restaurants(data):
    for restaurant in data:
        new_restaurant = Restaurante.objects.create(name= restaurant['name'])


def seed():
    # delete_all()
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        if Categoria.objects.count() == 0:
            create_categories(data['categories'])

        if Cozinheiro.objects.count() == 0 or Degustador.objects.count() == 0 or Editor.objects.count() == 0:
            create_users(data['people'])
            
        if Ingrediente.objects.count() == 0:
            create_ingredients(data['ingredients'])
            
        if Restaurante.objects.count()  == 0:
            create_restaurants(data['restaurants'])
    
