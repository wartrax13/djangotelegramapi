from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is the bot app.")

def prova(request):
    return HttpResponse("Isso é uma herança no django")

# Create your views here.
