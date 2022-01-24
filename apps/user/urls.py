from django.conf.urls import url
from .views import *

urlpatterns = [
    # url(r'^$', UserInfoView.as_view(), name='user_info'),

    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^edit$', EditView.as_view(), name='edit'),

]

app_name = 'user'
