from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'index.html', context)

def add_movie(request):
    # print(request.POST)
    Movie.objects.create(
        title = request.POST['title'],
        director = request.POST['director']
    )
    return redirect('/')

def delete(request, movie_id):
    movie_to_delete = Movie.objects.get(id=movie_id)
    movie_to_delete.delete()
    return redirect('/')
    
    
    

# def new_func():
#     return redirect('/')
