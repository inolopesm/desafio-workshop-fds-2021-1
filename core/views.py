from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm

class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'core/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryListView(ListView):
    model = Category

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'core/category_form.html'
    success_url = reverse_lazy('category-list')
