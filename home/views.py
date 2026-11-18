
from django.shortcuts import render


def index(request):
    contexto = {
        'title': 'Página Inicial',
        'message': 'Este é meu primeiro template Django!',
        'user_name': 'Guilherme'
    }

    return render(request, 'index.html', contexto)


def sobre(request):
    contexto = {
        'title': 'Sobre Nós',
        'message': 'Esta página apresenta informações sobre o projeto.'
    }

    return render(request, 'sobre.html', contexto)


def contato(request):
    contexto = {
        'title': 'Contato',
        'message': 'Entre em contato conosco!'
    }

    return render(request, 'contato.html', contexto)