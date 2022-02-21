from django.conf.urls import url
from music.views import MusicView, MusicTypeView

urlpatterns = [
    url(r'type/$', MusicTypeView.as_view()),
    url(r'$', MusicView.as_view()),

    # url(r'^detail/(?P<pizza_id>\d+)$', DetailView.as_view(), name='detail'),

    # url(r'^search$', SearchView.as_view(), name='search'),
    #
    # url(r'^leaderboard$', LeaderboardView.as_view(), name='leaderboard'),
]

app_name = 'music'
