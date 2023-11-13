import uuid
from django.db import models
from django.urls import reverse

class PrimitiveModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class User(PrimitiveModel):
    name = models.CharField(blank= True)
    email = models.EmailField(blank= True)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.CharField(max_length=11, unique=True)
    
    def custom_employee_display(self):
        role = ''
        
        if hasattr(self, 'cozinheiro'):
            role = 'Cozinheiro'
        elif hasattr(self, 'degustador'):
            role = 'Degustador'
        elif hasattr(self, 'editor'):
            role = 'Editor'
        
        if len(role)>0:
            return f"{role} - {self.name}"
        
        return f"{self.name}"
    
    def __str__(self) -> str:
        return self.name


class Cozinheiro(User):
    class Meta:
        verbose_name = 'Cozinheiro'
        
    chef_name = models.CharField(max_length=80, blank=True, default='')
    
    def get_absolute_url(self):
        return reverse('cheff-detail', args=[str(self.cpf)])
    
    def __str__(self) -> str:
        return super().name


class Degustador(User):
    class Meta:
        verbose_name = 'Degustador'
        verbose_name_plural  = 'Degustadores'
    
    def get_absolute_url(self):
        return reverse('taster-detail', args=[str(self.cpf)])
    
    def __str__(self) -> str:
        return super().name


class Editor(User):
    class Meta:
        verbose_name = 'Editor'
        verbose_name_plural  = 'Editores'
    
    def get_absolute_url(self):
        return reverse('editor-detail', args=[str(self.cpf)])
    
    def __str__(self) -> str:
        return super().name


class Categoria(PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField()
    description = models.CharField()
    
    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.code)])
    
    def __str__(self) -> str:
        return self.name


class Livro(PrimitiveModel):
    title = models.CharField(max_length=200, unique=True)
    isbn_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('livro-detail', args=[str(self.isbn_code)])
    
    def __str__(self) -> str:
        return self.title


class Ingrediente(PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(default='')
    
    def get_absolute_url(self):
        return reverse('ingrediente-detail', args=[str(self.code)])
    
    def __str__(self) -> str:
        return self.name


class Receita(PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    serving_amount = models.IntegerField(default=1)
    description = models.CharField(default='', blank= True)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    chef = models.ForeignKey(Cozinheiro, on_delete=models.CASCADE)
    book = models.ForeignKey(Livro, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('receita-detail', args=[str(self.code)])
    
    def __str__(self) -> str:
        return self.name



class Restaurante(PrimitiveModel):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200, unique=True)
    
    def get_absolute_url(self):
        return reverse('restaurante-detail', args=[str(self.code)])
    
    def __str__(self) -> str:
        return self.name


class Porcao(PrimitiveModel):
    class Meta:
        verbose_name = 'Porção'
        verbose_name_plural = 'Porções'
        
    ingredient = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    ingredient_amount = models.IntegerField(null= True, blank= True)
    measurement = models.CharField(null=True, blank=True)
    recipe = models.ForeignKey(Receita, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.ingredient.name + '-' + self.recipe.name
    
    def get_absolute_url(self):
        return reverse('porcao-list')


class Contrato(PrimitiveModel):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.employee.name + '-' + self.restaurant.name
    
    def get_absolute_url(self):
        return reverse('validacao-list')
    
    def custom_employee_display(self):
        return f"{self.employee.name} - {self.employee.email}"


class Validacao(PrimitiveModel):
    class Meta:
        verbose_name = 'Validação'
        verbose_name_plural = 'Validações'
    
    grade = models.IntegerField()
    taster = models.ForeignKey(Degustador, on_delete= models.CASCADE)
    recipe = models.ForeignKey(Receita, on_delete= models.CASCADE)
    
    def __str__(self) -> str:
        return self.taster.name + '-' + self.recipe.name
    
    def get_absolute_url(self):
        return reverse('validacao-detail', args=[str(self.id)])