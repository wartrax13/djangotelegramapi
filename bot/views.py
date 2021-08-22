from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is the bot app.")

def prova(request):
    return HttpResponse("Isso é uma herança no django")

def opcao(request):
    return HttpResponse("Estou testando as opções do Django")

# Create your views here.
