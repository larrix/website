from django.http import HttpResponse

def index(request):
    return HttpResponse ("<h1>Esta es la homepage de la seccion Musica</h1>")