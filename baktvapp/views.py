from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def trending(request):
    return render(request, 'trending.html')


def videos(request):
    return render(request, 'videos.html')


def stories(request):
    return render(request, 'stories.html')


def memes(request):
    return render(request, 'memes.html')


def about(request):
    return render(request, 'about.html')