from django.views.generic import UpdateView
from django.urls import reverse_lazy
from ..models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Validacao, Contrato
from ..forms import AddBookForm, AddCategoryForm, CreatePorcaoForm, CreateContractForm, CreateValidationForm
from ..forms import UpdateCheffForm, UpdateTasterForm, UpdateEditorForm, UpdateIngredientForm, UpdateRecipeForm, UpdateRestaurantForm

class CheffUpdateView(UpdateView):
    model = Cozinheiro
    form_class = UpdateCheffForm
    template_name='create/user-create.html'
    
    def get_object(self, queryset=None):
        cpf = self.kwargs.get('cpf')
        res = self.model.objects.get(cpf=cpf)
        return res


class TasterUpdateView(UpdateView):
    model = Degustador
    form_class = UpdateTasterForm
    template_name='create/user-create.html'
    
    def get_object(self, queryset=None):
        cpf = self.kwargs.get('cpf')
        res = self.model.objects.get(cpf=cpf)
        return res


class EditorUpdateView(UpdateView):
    model = Editor
    form_class = UpdateEditorForm
    template_name='create/user-create.html'
    
    def get_object(self, queryset=None):
        cpf = self.kwargs.get('cpf')
        res = self.model.objects.get(cpf=cpf)
        return res


class CategoryUpdateView(UpdateView):
    model = Categoria
    form_class = AddCategoryForm
    template_name='create/category-create.html'
    
    def get_object(self, queryset=None):
        code = self.kwargs.get('code')
        res = self.model.objects.get(code=code)
        return res

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar categoria'
        context['action_label'] = 'Editar'
        
        return context


class BookUpdateView(UpdateView):
    model = Livro
    form_class = AddBookForm
    template_name='create/book-create.html'
    
    def get_object(self, queryset=None):
        code = self.kwargs.get('isbn_code')
        res = self.model.objects.get(isbn_code=code)
        return res

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class ContractUpdateView(UpdateView):
    model = Contrato
    form_class = CreateContractForm
    template_name='create/contract-create.html'
    success_url = reverse_lazy('contract-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['action_label'] = 'Editar'
        
        return context


class IngredientUpdateView(UpdateView):
    model = Ingrediente
    form_class = UpdateIngredientForm
    template_name='create/ingredient-create.html'
    
    def get_object(self, queryset=None):
        code = self.kwargs.get('code')
        res = self.model.objects.get(code=code)
        return res

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_label'] = 'Editar'
        context['title'] = 'Editar um ingrediente'
        
        return context


class RecipeUpdateView(UpdateView):
    model = Receita
    form_class = UpdateRecipeForm
    template_name='create/recipe-create.html'
    
    def get_object(self, queryset=None):
        code = self.kwargs.get('code')
        res = self.model.objects.get(code=code)
        return res

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_label'] = 'Editar'
        context['title'] = 'Editar uma receita'
        
        return context


class RestaurantUpdateView(UpdateView):
    model = Restaurante
    form_class = UpdateRestaurantForm
    template_name='create/restaurant-create.html'
    
    def get_object(self, queryset=None):
        code = self.kwargs.get('code')
        print(code)
        res = self.model.objects.get(code=code)
        print(res)
        return res

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_label'] = 'Editar'
        context['title'] = 'Editar um restaurante'
        
        return context


class PorcaoUpdateView(UpdateView):
    model = Porcao
    form_class = CreatePorcaoForm
    template_name='create/porcao-create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_label'] = 'Editar'
        context['title'] = 'Editar porção'
        
        return context


class ValidacaoUpdateView(UpdateView):
    model = Validacao
    form_class = CreateValidationForm
    template_name='create/validation-create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_label'] = 'Editar'
        context['title'] = 'Editar validação'
        
        return context
