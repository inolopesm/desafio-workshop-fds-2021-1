from django.views.generic import CreateView
from .models import Category

class CategoryCreateView(CreateView):
    model = Category
