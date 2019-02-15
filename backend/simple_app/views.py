# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import re
from collections import Counter

import urllib.request
import lxml.html
from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.views.generic.base import TemplateView

from simple_app.models import Message

headers={'User-Agent': 'Mozilla/5.0'}

class HomeRss(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        """
        generators style (values) = [ (expression) for (value) in (collection) ]
        antipattern usage [ .get( , "") ] if response empty
        """

        # nversia
        nvrs = urllib.request.urlopen('https://nversia.ru/news/index/')
        nvrs_read = lxml.html.fromstring(nvrs.read())
        title_nvrs = nvrs_read.xpath('//div[@class="material-body"]/a/text()')[:1]
        url_nvrs = nvrs_read.xpath('//div[@class="material-body"]/a/@href')[:1]
        context_nvrs = dict(zip(title_nvrs, url_nvrs))

        return render(request, 'index.html', {'context_nvrs':context_nvrs})
