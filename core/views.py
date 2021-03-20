from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Category, Product
from .forms import CategoryForm, ProductForm

class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'core/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryListView(ListView):
    model = Category

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category-list')

class CategoryDetailView(DetailView):
    model = Category

class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'core/product_form.html'
    success_url = reverse_lazy('product-list')

class ProductListView(ListView):
    model = Product

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product-list')

class ProductDetailView(DetailView):
    model = Product
