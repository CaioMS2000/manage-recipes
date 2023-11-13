from django import forms
from .models import Categoria, Cozinheiro, Degustador, Editor, Livro, Ingrediente, Receita, Restaurante, Porcao, Contrato, Validacao, User

class BaseUserFormMeta:
    fields = ("name", "email", "salary", "cpf",)
    
    widgets = {
        'password': forms.PasswordInput(attrs={'class': 'input input-bordered'}),
        'name': forms.TextInput(attrs={'class': 'input input-bordered'}),
        'email': forms.EmailInput(attrs={'class': 'input input-bordered'}),
        'salary': forms.NumberInput(attrs={'class': 'input input-bordered'}),
        'cpf': forms.TextInput(attrs={'class': 'input input-bordered'}),
    }
    
    
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'description': forms.TextInput(attrs={'class': 'input input-bordered'}),
        }
    
    
class AddCheffForm(forms.ModelForm):
    class Meta(BaseUserFormMeta):
        model = Cozinheiro
    
    
# class UpdateCheffForm(forms.ModelForm):
#     class Meta(BaseUserFormMeta):
#         model = Cozinheiro
        
#         fields = BaseUserFormMeta.fields + ('chef_name',)
#         widgets = {
#             'chef_name': forms.TextInput(attrs={'class': 'input input-bordered'}),
#             **BaseUserFormMeta.widgets
#         }
class UpdateCheffForm(forms.ModelForm):
    chef_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered'}))

    class Meta(BaseUserFormMeta):
        model = Cozinheiro
        fields = BaseUserFormMeta.fields + ('chef_name',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        receitas = Receita.objects.filter(chef= self.instance)
        if receitas.count() < 5:# apenas chefs que ja produziram pelo menos 5 receitas podem ter um título especial de chef
            del self.fields['chef_name']
    
    
class AddTasterForm(forms.ModelForm):
    class Meta(BaseUserFormMeta):
        model = Degustador


class UpdateTasterForm(AddTasterForm):
    pass
    
    
class AddEditorForm(forms.ModelForm):
    class Meta(BaseUserFormMeta):
        model = Editor


class UpdateEditorForm(AddEditorForm):
    pass


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ("title", "editor")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'editor': forms.Select(attrs={'class': 'select'}),
        }


class AddIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ("name", "description")
        widgets = {
        'name': forms.TextInput(attrs={'class': 'input input-bordered'}),
        'description': forms.TextInput(attrs={'class': 'input input-bordered'}),
    }


class UpdateIngredientForm(AddIngredientForm):
    pass


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ("name", "serving_amount", "description", "category", "chef", "book")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'serving_amount': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'description': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'category': forms.Select(attrs={'class': 'select'}),
            'chef': forms.Select(attrs={'class': 'select'}),
            'book': forms.Select(attrs={'class': 'select'}),
        }


class UpdateRecipeForm(AddRecipeForm):
    pass


class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ("name",)
        widgets = {
        'name': forms.TextInput(attrs={'class': 'input input-bordered'}),
    }


class UpdateRestaurantForm(AddRestaurantForm):
    pass



class CreateContractForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'select'}),
        label="Employee",
        to_field_name='id',
        empty_label='Selecione',
        required=True,
        initial=None,
    )
    
    restaurant = forms.ModelChoiceField(
        queryset=Restaurante.objects.all(),
        widget=forms.Select(attrs={'class': 'select'}),
        label="Restaurant",
        to_field_name='id',
        empty_label='Selecione',
        required=True,
        initial=None,
    )

    def __init__(self, *args, **kwargs):
        super(CreateContractForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = User.objects.all()
        self.fields['employee'].label_from_instance = lambda obj: obj.custom_employee_display()

    class Meta:
        model = Contrato
        fields = ['employee', 'restaurant']


class CreatePorcaoForm(forms.ModelForm):
    class Meta:
        model= Porcao
        fields = ['ingredient', 'ingredient_amount', 'measurement', 'recipe']
        
        widgets = {
            'ingredient': forms.Select(attrs={'class': 'select'}),
            'ingredient_amount': forms.NumberInput(attrs={'class': 'input input-bordered'}),
            'measurement': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'recipe': forms.Select(attrs={'class': 'select'}),
        }


class CreateValidationForm(forms.ModelForm):
    class Meta:
        model= Validacao
        fields = ['grade', 'taster', 'recipe']
        
        widgets = {
            'grade': forms.NumberInput(attrs={'class': 'input input-bordered'}),
            'taster': forms.Select(attrs={'class': 'select'}),
            'recipe': forms.Select(attrs={'class': 'select'}),
        }
    
    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if grade < 0 or grade > 5:
            raise forms.ValidationError("A nota deve estar entre 0 e 5.")
        return grade