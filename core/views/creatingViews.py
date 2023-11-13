from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.apps import apps
from ..models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato, Validacao
from ..forms import AddCheffForm, AddTasterForm, AddEditorForm, AddBookForm, AddIngredientForm, AddRecipeForm, AddRestaurantForm, AddCategoryForm, CreateContractForm, CreatePorcaoForm, CreateValidationForm

class CategoryCreateView(CreateView):
    model = Categoria
    form_class = AddCategoryForm
    template_name='create/category-create.html'

class UserCreateView(CreateView):
    model = Cozinheiro
    form_class = AddCheffForm
    template_name='create/user-create.html'


class TasterCreateView(CreateView):
    model = Degustador
    form_class = AddTasterForm
    template_name='create/user-create.html'


class EditorCreateView(CreateView):
    model = Editor
    form_class = AddEditorForm
    template_name='create/user-create.html'


class LivroCreateView(CreateView):
    model = Livro
    form_class = AddBookForm
    template_name='create/book-create.html'


class IngredienteCreateView(CreateView):
    model = Ingrediente
    form_class = AddIngredientForm
    template_name='create/ingredient-create.html'


class ReceitaCreateView(CreateView):
    model = Receita
    form_class = AddRecipeForm
    template_name='create/recipe-create.html'


class RestauranteCreateView(CreateView):
    model = Restaurante
    form_class = AddRestaurantForm
    template_name='create/restaurant-create.html'


class PorcaoCreateView(CreateView):
    model = Porcao
    form_class = CreatePorcaoForm
    template_name='create/porcao-create.html'


class ContractCreateView(CreateView):
    model = Contrato
    form_class = CreateContractForm
    template_name='create/contract-create.html'
    success_url = reverse_lazy('contract-list')



class ValidationCreateView(CreateView):
    model = Validacao
    form_class = CreateValidationForm
    template_name='create/validation-create.html'

