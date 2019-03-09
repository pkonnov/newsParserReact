import json
import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from . import models


class NewsUrlsType(DjangoObjectType):
    class Meta:
        model = models.NewsUrls
        filter_fields = {'created_at': ['icontains']}
        interfaces = (graphene.Node, )

class Query(graphene.AbstractType):

    all_news_urls = DjangoFilterConnectionField(NewsUrlsType)

    def resolve_all_news_urls(self, args, **kwargs):
        return models.NewsUrls.objects.order_by('-created_at')
