from django.forms import ModelForm, ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Category, Product

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': _('Nome')}

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget.attrs['min'] = 0
        self.fields['value'].widget.attrs['step'] = 0.01
        self.fields['amount'].widget.attrs['min'] = 0

    class Meta:
        model = Product
        fields = ['name', 'value', 'amount', 'category']
        labels = {'name': _('Nome'), 'value': _('Valor'), 'amount': _('Quantidade'), 'category': _('Categoria')}

    def clean_value(self):
        value = self.cleaned_data['value']
        if value < 0:
            raise ValidationError('Valor não pode ser menor que 0')
        return value

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise ValidationError('Quantidade não pode ser menor que 0')
        return amount
