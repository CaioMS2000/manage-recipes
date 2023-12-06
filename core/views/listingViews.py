from typing import Any
from django.shortcuts import render
from django.db.models import Count
from django.views.generic import TemplateView, ListView
from django.apps import apps
from ..models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Contrato, Porcao, Validacao

class Index(TemplateView):
    template_name='index.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        models = apps.get_models()
        my_models = [model for model in models if not model.__module__.startswith("django.")]
        models_names = []
        
        for model in my_models:
            if model.__name__ not in ["User", "PrimitiveModel"]:
                names = ['', '']
                try:
                    names[0] = model._meta.verbose_name
                except AttributeError:
                    names[0] = model.__name__
                
                names[1] = model.__name__
                models_names.append(names)

        context = super().get_context_data(**kwargs)
        context['models'] = models_names
        
        return context


class CategoryListView(ListView):
    model = Categoria
    template_name='list/category-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorias = self.model.objects.all()
        context['categorias'] = categorias
        
        return context


class ContractListView(ListView):
    model = Contrato
    template_name='list/contract-list.html'
    success_url= 'contract-list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class CheffListView(ListView):
    model = Cozinheiro
    template_name='list/cheff-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtém os 5 cozinheiros com mais receitas
        top_cozinheiros = Cozinheiro.objects.annotate(num_receitas=Count('receita')).order_by('num_receitas')[:5]
        for cozinheiro in top_cozinheiros:
            print(f"{cozinheiro.name} - {cozinheiro.num_receitas} receitas")
        
        context['top_cheffs'] = top_cozinheiros
        
        cheffs = self.model.objects.all()
        context['cheffs'] = cheffs
        
        
        return context


class TasterListView(ListView):
    model = Degustador
    template_name='list/taster-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class EditorListView(ListView):
    model = Editor
    template_name='list/editor-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class LivroListView(ListView):
    model = Livro
    template_name='list/book-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class IngredienteListView(ListView):
    model = Ingrediente
    template_name='list/ingredient-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class ReceitaListView(ListView):
    model = Receita
    template_name='list/recipe-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class RestauranteListView(ListView):
    model = Restaurante
    template_name='list/restaurant-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class PorcaoListView(ListView):
    model = Porcao
    template_name='list/porcao-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class ValidationListView(ListView):
    model = Validacao
    template_name='list/validation-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
