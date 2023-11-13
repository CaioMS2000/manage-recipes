from django.views.generic import DetailView
from django.apps import apps
from ..models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato, Validacao

class CategoryDetailView(DetailView):
    model = Categoria
    template_name='detail/category-detail.html'

    def get_object(self, **kwargs):
        code = self.kwargs.get("code")
        
        return self.model.objects.get(code= code)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        category = self.get_object()
        context['recipes']= Receita.objects.filter(category__code= category.code)
        context['prev_page_link'] = '/categoria'
        
        return context


class CheffDetailView(DetailView):
    model = Cozinheiro
    template_name='detail/cheff-detail.html'

    def get_object(self):
        
        return self.model.objects.get(cpf=self.kwargs.get("cpf"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        chef = self.get_object()
        context['recipes'] = Receita.objects.filter(chef__cpf= chef.cpf)
        context['prev_page_link'] = '/cozinheiro'
        
        return context


class TasterDetailView(DetailView):
    model = Degustador
    template_name='detail/taster-detail.html'

    def get_object(self):
        
        return self.model.objects.get(cpf=self.kwargs.get("cpf"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        taster = self.get_object()
        avaliacoes = Validacao.objects.filter(taster= taster)
        context['avaliacoes'] = avaliacoes
        
        context['prev_page_link'] = '/degustador'
        
        return context


class EditorDetailView(DetailView):
    model = Editor
    template_name='detail/editor-detail.html'

    def get_object(self):
        
        return self.model.objects.get(cpf=self.kwargs.get("cpf"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        editor = self.get_object()
        context['books'] = Livro.objects.filter(editor__cpf= editor.cpf)
        context['prev_page_link'] = '/editor'
        
        return context


class LivroDetailView(DetailView):
    model = Livro
    template_name='detail/book-detail.html'

    def get_object(self):
        
        return self.model.objects.get(isbn_code=self.kwargs.get("isbn_code"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        book = self.get_object()
        context['recipes']= Receita.objects.filter(book__title= book.title)
        context['editor'] = book.editor
        context['prev_page_link'] = '/livro'
        
        return context


class IngredienteDetailView(DetailView):
    model = Ingrediente
    template_name='detail/ingredient-detail.html'

    def get_object(self):
        
        return self.model.objects.get(code=self.kwargs.get("code"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['prev_page_link'] = '/ingrediente'
        
        return context


class ContractDetailView(DetailView):
    model = Contrato
    template_name='detail/contrato-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        contrato = self.get_object()
        quando = contrato.created_at
        context['data_de_criacao'] = f'{quando.day}/{quando.month}/{quando.year}'
        context['prev_page_link'] = '/contrato'
        
        return context


class PorcaoDetailView(DetailView):
    model = Porcao
    template_name='detail/porcao-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        porcao = self.get_object()
        context['prev_page_link'] = '/porcao'
        context['ingrediente'] = porcao.ingredient.name
        context['ingredient_amount'] = porcao.ingredient_amount
        context['measurement'] = porcao.measurement
        
        return context


class ValidacaoDetailView(DetailView):
    model = Validacao
    template_name='detail/validacao-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['prev_page_link'] = '/validacao'
        
        return context


class RestauranteDetailView(DetailView):
    model = Restaurante
    template_name='detail/restaurant-detail.html'

    def get_object(self):
        
        return self.model.objects.get(code=self.kwargs.get("code"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        restaurante = self.get_object()
        contratos = Contrato.objects.filter(restaurant=restaurante)

        cozinheiros = []
        degustadores = []
        editores = []

        for contrato in contratos:
            if hasattr(contrato.employee, 'cozinheiro'):
                cozinheiros.append(contrato.employee)
            elif hasattr(contrato.employee, 'degustador'):
                degustadores.append(contrato.employee)
            elif hasattr(contrato.employee, 'editor'):
                editores.append(contrato.employee)

        print(cozinheiros)
        print(degustadores)
        print(editores)
        
        context['cozinheiros'] = cozinheiros
        context['degustadores'] = degustadores
        context['editores'] = editores
        
        context['prev_page_link'] = '/restaurante'
        
        return context


class RecipeDetailView(DetailView):
    model = Receita
    template_name='detail/recipe-detail.html'

    def get_object(self):
        
        return self.model.objects.get(code=self.kwargs.get("code"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        receita = self.get_object()
        quando = receita.created_at
        porcoes = Porcao.objects.filter(recipe= receita)
        
        context['data_de_criacao'] = f'{quando.day}/{quando.month}/{quando.year}'
        context['prev_page_link'] = '/receita'
        context['porcoes'] = porcoes
        
        return context

