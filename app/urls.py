from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('listar_tarefas',listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefas',cadastrar_tarefas, name='cadastrar_tarefas'),
    path('editar_tarefas/<int:id>',editar_tarefa, name='editar_tarefas'),
    path('remover_tarefas/<int:id>',remover_tarefa, name='remover_tarefas'),
]