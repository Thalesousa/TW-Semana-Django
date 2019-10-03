from django.shortcuts import render


def cadastra_usuario(request):
    return render(request, 'usuarios/form_usuario.html')