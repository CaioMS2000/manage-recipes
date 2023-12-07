from typing import Any
from django.shortcuts import render
from django.db.models import Count
from django.views.generic import TemplateView, ListView
from django.apps import apps
from ..models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Contrato, Porcao, Validacao
from ..forms import ReceitaFilterForm

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
        
        # categorias_com_receitas = Categoria.objects.annotate(num_receitas=Count('receita'))

        # context['categorias_com_receitas'] = categorias_com_receitas
        
        categorias = self.model.objects.all()
        categorias = self.model.objects.annotate(num_receitas=Count('receita'))
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
        
        context['form'] = ReceitaFilterForm(self.request.GET)
        context['form_options'] = Ingrediente.objects.all()
        
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        print(queryset)
        # Obter parâmetros de filtro do formulário
        ingredientes_validos = self.request.GET.getlist('ingrediente', '')
        
        if '-1' in ingredientes_validos:
            ingredientes_validos.remove('-1')
            
        ingredientes_validos = [int(x) for x in ingredientes_validos]
        print('##')
        print(ingredientes_validos)
        print('##')
        

        if not ingredientes_validos:
            print('SEM FILTRAGEM')
            return queryset
        
        print('\n\n')        
        for objeto in queryset:
            print('atual')
            print(objeto)
            print(objeto.id)
            print('\n\n')
            # cada validação
            # for att in objeto.__dict__:
            #     print(att)
            
            print('\n')
            # receita da atual validação
            receita = Receita.objects.get(id= objeto.recipe_id)
            print(f'receita da validação {objeto.id}')
            print(receita)
            
            print('\n')
            # porções dessa receita
            porcoes = Porcao.objects.filter(recipe_id= objeto.recipe_id)
            print(f'porcoes')
            print(porcoes)
            
            ingredientes = []
            flag = True
            for porcao in porcoes:
                ingredientes.append(porcao.ingredient)
            
            print('\n')
            # ingredientes da receita
            print(f'ingredientes')
            print(ingredientes)
            
            print('\n')
            # ids dos ingredientes da receita
            ingredientes_ids = [int(i.id) for i in ingredientes]
            print(f'ingredientes - ids')
            print(ingredientes_ids)
            
            print('\n')
            for x in ingredientes_validos:
                print(f'avaliando {x} em')
                print(ingredientes_ids)
                
                if x  not in ingredientes_ids:
                    print(f'{x} n esta em')
                    print(ingredientes_ids)
                    flag = False
            
            print('\n')        
            print(f'flag: {flag}')
            
            if flag == False:
                print(f'excluindo {objeto.id}')
                print(objeto)
                queryset = queryset.exclude(id= objeto.id)

        print('\n\n')
        print(queryset)
        return queryset
    