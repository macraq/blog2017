# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Article

from django.core.exceptions import ObjectDoesNotExist

def home(request):
    context = {
        'title': 'Strona główna',
        'articles': Article.objects.order_by('title')
    }
    return render(request, 'post_list.html', context)
    
def post_show(request, post_id):
    article = Article.objects.get(pk=post_id)
    if not article:
        raise ObjectDoesNotExist
        
    return render(request, 'post_show.html', {
        'article':article
    })