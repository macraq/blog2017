# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Commentator, Comment

class CommentAdmin(admin.ModelAdmin):
    models = Comment
    list_display = ['title', 'visible']
        
admin.site.register(Comment)
admin.site.register(Commentator)
