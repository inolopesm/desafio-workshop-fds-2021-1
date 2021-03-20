from django.urls import path
from .views import CategoryCreateView

urlpatterns = [
    path('categories/create/', CategoryCreateView.as_view()),
]