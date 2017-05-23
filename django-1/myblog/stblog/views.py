# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models
# Create your views here.
def index(request):
    articles = models.stArticle.objects.all()
    return render(request,'stblog/index_page.html',{'articles':articles})

def article_page(request,article_id):
    article = models.stArticle.objects.get(pk=article_id)
    return render(request, 'stblog/article_page.html', {'article': article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'stblog/edit_page.html')
    else:
        article = models.stArticle.objects.get(pk=article_id)
        return render(request, 'stblog/edit_page.html',{'article':article})

def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id =='0':
        models.stArticle.objects.create(title=title,content=content)
        articles = models.stArticle.objects.all()
        return render(request, 'stblog/index_page.html', {'articles': articles})
    else:
        article=models.stArticle.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'stblog/article_page.html', {'article': article})
