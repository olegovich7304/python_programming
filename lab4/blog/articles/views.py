from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import Article

def archive(request):
    return render(request, 'archive.html', {
        "posts": Article.objects.all()
    })

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Article not found")

    return render(request, 'article.html', {
        "post": post
    })
