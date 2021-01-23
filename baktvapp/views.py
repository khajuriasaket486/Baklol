from django.http import HttpResponse
from django.shortcuts import render
from videoapp.models import VideoModel
from articleapp.models import ArticleModel
from authorapp.models import AuthorModel
from memeapp.models import MemeModel

# Create your views here.
def homepage(request):
    videoLink = VideoModel.objects.values_list()
    article = ArticleModel.objects.values_list()
    author = ArticleModel.objects.values_list()
    meme = MemeModel.objects.values_list()

    context = {
        videoLink:videoLink,
        article:article,
        author:author,
        meme:meme,

    }

    return render(request, 'homepage.html', context)


def trending(request):
    return render(request, 'trending.html')


def videos(request):
    qs = VideoModel.objects.values_list()
    var = ''
    for x in qs:
        if x[2] is not None:
            var = x[2]
        print(var)
    return render(request, 'videos.html', context={'link':var})


def stories(request):
    return render(request, 'stories.html')


def memes(request):
    return render(request, 'memes.html')


def about(request):
    return render(request, 'about.html')