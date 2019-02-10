from django.conf.urls import url

from simple_app.views import HomeRss

urlpatterns = [
    # path('', views.rss_lenta, name='rss_lenta'),
    # path('rss/', HomeRss.as_view(template_name="rss_lenta.html")),
    url('', HomeRss.as_view(template_name="index.html")),
    # path('sarinform/', views.soup_parser, name='sarinform'),
    # path('sarbc/', views.soup_parser0, name='sarbc'),
    # path('api/news/', NewsUrlsCreate.as_view() ),
    #path('logs_parser/', views.logs_parser, name='logs_parser'),
]
