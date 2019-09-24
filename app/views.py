from django.shortcuts import render


def listar_tarefas(request):
    nome_tarefa = 'Assistir a semana de python e django'
    return render(request,'tarefas/listar_tarefas.html', {'nome_tarefa': nome_tarefa})