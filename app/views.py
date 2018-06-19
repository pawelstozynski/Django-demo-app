from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from .forms import *
from .models import *


def index(request):
    articles = Article.objects.all()
    return render(request, 'article/index.html', {'articles':articles})


def article_show(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article/show.html', {'article':article})


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm()
        return render(request, 'article/create.html', {'form':form})


def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm(instance=article)
        return render(request, 'article/edit.html', {'form':form, 'article':article})


def article_delete(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return redirect('index')
    else:
        return HttpResponse('Not allowed')