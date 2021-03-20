from django.urls import path
from .views import CategoryCreateView, CategoryListView, CategoryUpdateView

urlpatterns = [
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/edit', CategoryUpdateView.as_view(), name='category-update'),
]