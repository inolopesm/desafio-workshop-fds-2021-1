from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': _('Nome')}