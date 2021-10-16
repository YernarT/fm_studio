from django.conf.urls import url
from .views import *

urlpatterns = [
    # url(r'^$', UserInfoView.as_view(), name='user_info'),

    url(r'^log$', LoginView.as_view(), name='log'),
    url(r'^reg$', RegisterView.as_view(), name='reg'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),

]

app_name = 'user'
