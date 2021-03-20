from django.urls import path
from .views import CategoryCreateView

urlpatterns = [
    path('create/', CategoryCreateView.as_view()),
]