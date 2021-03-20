from django.urls import path
from .views import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDetailView, ProductCreateView, ProductListView, ProductUpdateView, ProductDetailView

urlpatterns = [
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/edit', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
]