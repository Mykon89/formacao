from django.urls import path 
from receitas.views import index

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receita', views.receita, name='receita')
]