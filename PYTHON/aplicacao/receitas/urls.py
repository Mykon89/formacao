from django.urls import path 
from receitas.views import index

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita')
]