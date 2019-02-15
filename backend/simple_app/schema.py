import json
import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from . import models



class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message
        filter_fields = {'message': ['icontains']}
        interfaces = (graphene.Node, )


class NewsUrlsType(DjangoObjectType):
    class Meta:
        model = models.NewsUrls
        filter_fields = {'created_at': ['icontains']}
        interfaces = (graphene.Node, )


class CreateMessage(graphene.Mutation):
    class Input:
        message = graphene.String()

    form_errors = graphene.String()
    message = graphene.Field(lambda: MessageType)

    @staticmethod
    def mutate(root, args, context, info):
        if not args.get('message').strip():
            return CreateMessage(
                form_errors=json.dumps('Please enter a message!'))
        message = models.Message.objects.create(message=args.get('message'))
        return CreateMessage(message=message, form_errors=None)


class Mutation(graphene.AbstractType):
    create_message = CreateMessage.Field()


class Query(graphene.AbstractType):
    all_messages = DjangoFilterConnectionField(MessageType)
    all_news_urls = DjangoFilterConnectionField(NewsUrlsType)

    message = graphene.Field(MessageType, id=graphene.ID())
    news = graphene.Field(NewsUrlsType)

    @staticmethod
    def resolve_all_messages(self, args, context, info):
        orderBy = args.get("orderBy", None)
        if orderBy:
            return models.Message.objects.order_by(*orderBy)
        else:
            return models.Message.objects.all()

    @staticmethod
    def resolve_all_news_urls(self, args, context, info):
        return models.NewsUrls.objects.order_by('-created_at')

    @staticmethod
    def resolve_message(self, args, context, info):
        from graphql_relay.node.node import from_global_id
        pk = from_global_id(args.get('id'))[1]
        return models.Message.objects.get(pk=pk)


