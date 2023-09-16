from django.shortcuts import render
from BBlog.models.article import *

def base(request):
    articles = Article.objects.all()[:3]

    context = {
        'articles':articles,
    }

    return render(request, 'website/landing.html', context)