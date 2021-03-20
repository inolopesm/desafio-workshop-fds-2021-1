from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Category, Product

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': _('Nome')}

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'value', 'amount', 'category']
        labels = {'name': _('Nome'), 'value': _('Valor'), 'amount': _('Quantidade'), 'category': _('Categoria')}
