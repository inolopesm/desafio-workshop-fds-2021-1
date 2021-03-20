from django.views.generic import CreateView
from .forms import CategoryForm

class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'core/category_form.html'
    success_url = '/categories/'
