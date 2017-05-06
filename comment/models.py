# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

from main.models import Article
# Create your models here.

class Commentator(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(User, unique=True, null=False, blank=False)

class Comment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    visible = models.BooleanField(default=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    commentator = models.ForeignKey(Commentator, on_delete=models.CASCADE)