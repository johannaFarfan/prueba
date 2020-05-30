from django.shortcuts import render
from .models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'courses': courses})


def saludo(request):
    return HttpResponse("Hola Mundo!")