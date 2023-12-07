from django.urls import path, include
from .views import Index, CategoryListView, CheffListView, TasterListView, EditorListView, LivroListView, IngredienteListView, ReceitaListView, RestauranteListView, ContractListView, PorcaoListView, ValidationListView
from .views import CategoryDetailView, CheffDetailView, TasterDetailView, EditorDetailView, LivroDetailView, IngredienteDetailView, RecipeDetailView, RestauranteDetailView, PorcaoDetailView, ValidacaoDetailView, ContractDetailView
from .views import CategoryCreateView, UserCreateView, TasterCreateView, EditorCreateView, LivroCreateView, IngredienteCreateView, ReceitaCreateView, RestauranteCreateView, PorcaoCreateView, ContractCreateView, ValidationCreateView
from .views import CheffUpdateView, TasterUpdateView, EditorUpdateView, CategoryUpdateView, BookUpdateView, IngredientUpdateView, RestaurantUpdateView, RecipeUpdateView, PorcaoUpdateView, ValidacaoUpdateView, ContractUpdateView
from .views import ChefDeleteView, TasterDeleteView, EditorDeleteView, CategoryDeleteView, IngredientDeleteView, RecipeDeleteView, RestaurantDeleteView, BookDeleteView, PorcaoDeleteView, ValidacaoDeleteView, ContractDeleteView
from .seed import seed

# seed()

urlpatterns = [
    path('', Index.as_view(), name= 'main'),
    
    path('categoria', CategoryListView.as_view(), name= 'category-list'),
    path('cozinheiro', CheffListView.as_view(), name= "cheff-list"),
    path('degustador', TasterListView.as_view(), name= "taster-list"),
    path('editor', EditorListView.as_view(), name= "editor-list"),
    path('livro', LivroListView.as_view(), name= 'book-list'),
    path('ingrediente', IngredienteListView.as_view(), name= 'ingredient-list'),
    path('receita', ReceitaListView.as_view(), name= 'recipe-list'),
    path('restaurante', RestauranteListView.as_view(), name= 'restaurant-list'),
    path('contrato', ContractListView.as_view(), name= 'contract-list'),
    path('porcao', PorcaoListView.as_view(), name= 'porcao-list'),
    path('validacao', ValidationListView.as_view(), name= 'validacao-list'),
    
    path('categoria/criar', CategoryCreateView.as_view()),
    path('cozinheiro/criar', UserCreateView.as_view()),
    path('degustador/criar', TasterCreateView.as_view()),
    path('editor/criar', EditorCreateView.as_view()),
    path('livro/criar', LivroCreateView.as_view()),
    path('ingrediente/criar', IngredienteCreateView.as_view()),
    path('receita/criar', ReceitaCreateView.as_view()),
    path('restaurante/criar', RestauranteCreateView.as_view()),
    path('porcao/criar', PorcaoCreateView.as_view()),
    path('contrato/criar', ContractCreateView.as_view()),
    path('validacao/criar', ValidationCreateView.as_view()),
    
    path('cozinheiro/remover/<int:pk>', ChefDeleteView.as_view()),
    path('degustador/remover/<int:pk>', TasterDeleteView.as_view()),
    path('editor/remover/<int:pk>', EditorDeleteView.as_view()),
    path('categoria/remover/<str:code>', CategoryDeleteView.as_view()),
    path('ingrediente/remover/<str:code>', IngredientDeleteView.as_view()),
    path('receita/remover/<str:code>', RecipeDeleteView.as_view()),
    path('restaurante/remover/<str:code>', RestaurantDeleteView.as_view()),
    path('livro/remover/<str:isbn_code>', BookDeleteView.as_view()),
    path('porcao/remover/<int:pk>', PorcaoDeleteView.as_view()),
    path('validacao/remover/<int:pk>', ValidacaoDeleteView.as_view()),
    path('contrato/remover/<int:pk>', ContractDeleteView.as_view()),
    
    path('categoria/editar/<uuid:code>', CategoryUpdateView.as_view()),
    path('cozinheiro/editar/<str:cpf>', CheffUpdateView.as_view()),
    path('degustador/editar/<str:cpf>', TasterUpdateView.as_view()),
    path('editor/editar/<str:cpf>', EditorUpdateView.as_view()),
    path('livro/editar/<str:isbn_code>', BookUpdateView.as_view()),
    path('ingrediente/editar/<str:code>', IngredientUpdateView.as_view()),
    path('receita/editar/<str:code>', RecipeUpdateView.as_view()),
    path('restaurante/editar/<str:code>', RestaurantUpdateView.as_view()),
    path('porcao/editar/<int:pk>', PorcaoUpdateView.as_view()),
    path('validacao/editar/<int:pk>', ValidacaoUpdateView.as_view()),
    path('contrato/editar/<int:pk>', ContractUpdateView.as_view()),
    
    path('categoria/<uuid:code>', CategoryDetailView.as_view(), name= "category-detail"),
    path('cozinheiro/<str:cpf>', CheffDetailView.as_view(), name= "cheff-detail"),
    path('degustador/<str:cpf>', TasterDetailView.as_view(), name= "taster-detail"),
    path('editor/<str:cpf>', EditorDetailView.as_view(), name= "editor-detail"),
    path('livro/<str:isbn_code>', LivroDetailView.as_view(), name= "livro-detail"),
    path('ingrediente/<uuid:code>', IngredienteDetailView.as_view(), name= "ingrediente-detail"),
    path('receita/<uuid:code>', RecipeDetailView.as_view(), name= "receita-detail"),
    path('restaurante/<uuid:code>', RestauranteDetailView.as_view(), name= "restaurante-detail"),
    path('porcao/<int:pk>', PorcaoDetailView.as_view(), name= "porcao-detail"),
    path('validacao/<int:pk>', ValidacaoDetailView.as_view(), name= "validacao-detail"),
    path('contrato/<int:pk>', ContractDetailView.as_view(), name= "contrato-detail"),
]