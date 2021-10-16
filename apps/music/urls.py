from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),

    # url(r'^detail/(?P<pizza_id>\d+)$', DetailView.as_view(), name='detail'),

    # url(r'^search$', SearchView.as_view(), name='search'),
]

app_name = 'music'
