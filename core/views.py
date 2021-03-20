from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm

class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'core/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryListView(ListView):
    model = Category
