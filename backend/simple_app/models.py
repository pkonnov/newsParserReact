# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Message(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.message


class NewsUrls(models.Model):
    site_url = models.CharField(max_length=50)
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
