from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
from django.template import loader
# Create your views here.

def index(request):
    movies_list = Movies.objects.all()
    print(movies_list)
    #template = loader.get_template('moviespg/index.html')
    context = {
        'movies_list': movies_list,
    }
    return render(request, 'moviespg/index.html', context)

