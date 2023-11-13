from django.views.generic import DeleteView
from ..models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato, User, Validacao
from django.urls import reverse_lazy

class UserDeleteBaseView(DeleteView):
    model = User
    template_name = 'delete/user_confirm_deletion.html'


class ChefDeleteView(UserDeleteBaseView, DeleteView):
    success_url = reverse_lazy('cheff-list')


class TasterDeleteView(UserDeleteBaseView):
    success_url = reverse_lazy('taster-list')


class EditorDeleteView(UserDeleteBaseView):
    success_url = reverse_lazy('editor-list')


class ObjectDeleteBaseView(DeleteView):
    template_name = 'delete/object_confirm_deletition.html'

    def get_object(self, queryset=None):
        code = self.kwargs.get('code')
        res = self.model.objects.get(code=code)
        return res


class CategoryDeleteView(ObjectDeleteBaseView):
    model = Categoria
    success_url = reverse_lazy('category-list')


class IngredientDeleteView(ObjectDeleteBaseView):
    model = Ingrediente
    success_url = reverse_lazy('ingredient-list')


class RecipeDeleteView(ObjectDeleteBaseView):
    model = Receita
    success_url = reverse_lazy('recipe-list')


class RestaurantDeleteView(ObjectDeleteBaseView):
    model = Restaurante
    success_url = reverse_lazy('restaurant-list')


class BookDeleteView(DeleteView):
    model = Livro
    template_name = 'delete/object_confirm_deletition.html'
    success_url = reverse_lazy('book-list')

    def get_object(self, queryset=None):
        code = self.kwargs.get('isbn_code')
        res = self.model.objects.get(isbn_code=code)
        return res


class PorcaoDeleteView(DeleteView):
    model = Porcao
    template_name = 'delete/object_confirm_deletition.html'
    success_url = reverse_lazy('porcao-list')


class ValidacaoDeleteView(DeleteView):
    model = Validacao
    template_name = 'delete/object_confirm_deletition.html'
    success_url = reverse_lazy('validacao-list')


class ContractDeleteView(DeleteView):
    model = Contrato
    template_name = 'delete/object_confirm_deletition.html'
    success_url = reverse_lazy('contract-list')
    