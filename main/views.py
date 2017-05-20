# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.shortcuts import render, redirect
from models import Article
from comment.forms import CommentForm

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
        
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commentator = request.user.commentator
            comment.created_date = timezone.now()
            comment.save()
            redirect('post_show', {'post_id':article.id})
    else:
        comment_form = CommentForm(initial={
            'article': post_id
        })
    
    return render(request, 'post_show.html', {
        'article':article,
        'comment_form':comment_form
    })