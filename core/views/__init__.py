from .listingViews import Index, CategoryListView, CheffListView, TasterListView, EditorListView, LivroListView, IngredienteListView, ReceitaListView, RestauranteListView, ContractListView, PorcaoListView, ValidationListView

from .detailingViews import CategoryDetailView, CheffDetailView, TasterDetailView, EditorDetailView, LivroDetailView, IngredienteDetailView, RecipeDetailView, RestauranteDetailView, PorcaoDetailView, ValidacaoDetailView, ContractDetailView

from .creatingViews import CategoryCreateView, UserCreateView, TasterCreateView, EditorCreateView, LivroCreateView, IngredienteCreateView, ReceitaCreateView, RestauranteCreateView, PorcaoCreateView, ContractCreateView, ValidationCreateView

from .updatingViews import CheffUpdateView, TasterUpdateView, EditorUpdateView, CategoryUpdateView, BookUpdateView, IngredientUpdateView, RestaurantUpdateView, RecipeUpdateView, PorcaoUpdateView, ValidacaoUpdateView, ContractUpdateView

from .deletingViews import ChefDeleteView, TasterDeleteView, EditorDeleteView, CategoryDeleteView, IngredientDeleteView, RecipeDeleteView, RestaurantDeleteView, BookDeleteView, PorcaoDeleteView, ValidacaoDeleteView, ContractDeleteView