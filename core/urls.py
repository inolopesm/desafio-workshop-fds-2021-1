from django.urls import path
from .views import CategoryCreateView, CategoryListView

urlpatterns = [
    path('categories/create/', CategoryCreateView.as_view()),
    path('categories/', CategoryListView.as_view()),
]