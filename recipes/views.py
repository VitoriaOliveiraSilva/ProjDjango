from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Vitoria de Oliveira', 
    })


def contato(request):
    return render(request, 'recipes/contato.html')  # /contato/


def sobre(request):
    return HttpResponse('Sobre nós!')  # /sobre/