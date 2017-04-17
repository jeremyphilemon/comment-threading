from django.shortcuts import render
from genre.models import Genre

def show_genres(request):
    return render(request, "genres.html",
                          {'nodes':Genre.objects.all()})
