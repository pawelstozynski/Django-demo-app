from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from ..forms import *
from ..models import *


@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article/list.html', {'articles':articles})


@require_POST
def article_search(request):
    search_string = request.POST['search']
    articles = Article.objects.filter(name__contains=search_string)
    return render(request, 'article/list.html', {'articles':articles})


@require_GET
def article_show(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article/show.html', {'article':article})


@require_http_methods(['GET', 'POST'])
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article-list')
    else:
        form = ArticleForm()
        return render(request, 'article/create.html', {'form':form})


@require_http_methods(['GET', 'POST'])
def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article-list')
    else:
        form = ArticleForm(instance=article)
        return render(request, 'article/edit.html', {'form':form, 'article':article})


@require_POST
def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('article-list')


@require_POST
def article_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comment = Comment(content=request.POST['comment'], article=article)
    comment.save()
    return redirect('article-show', article_id)


@require_POST
def article_comment_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('article-show', article_id)
    