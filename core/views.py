from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
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

class CategoryDeleteView(DeleteView):
    model = Category

class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'core/product_form.html'
    success_url = reverse_lazy('product-list')

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
        # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#icontains

        orderByValue = self.request.GET.get('orderBy', 'id')
        fieldName = self.request.GET.get('fieldName')
        fieldValue = self.request.GET.get('fieldValue')

        queryset = Product.objects.order_by(orderByValue)

        if fieldName and fieldValue:
            if fieldName == 'id':
                queryset = queryset.filter(id__icontains=int(fieldValue))
            elif fieldName == 'name':
                queryset = queryset.filter(name__icontains=fieldValue)
            elif fieldName == 'value':
                queryset = queryset.filter(value__icontains=float(fieldValue))
            elif fieldName == 'amount':
                queryset = queryset.filter(amount__icontains=int(fieldValue))

        return queryset

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product-list')

class ProductDetailView(DetailView):
    model = Product

class ProductDeleteView(DeleteView):
    model = Product
