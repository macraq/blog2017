# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    firstname = models.TextField(max_length=10)
    lastname = models.TextField(max_length=15)
    def __str__(self):
        return " ".join([self.firstname, self.lastname]).encode('utf-8').strip()

class Article(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return ("%s (%s)" % (self.title, self.author)).encode('utf-8').strip()
    
