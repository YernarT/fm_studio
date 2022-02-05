from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^edit$', EditView.as_view(), name='edit'),
    url(r'^edit/avatar$', EditAvatarView.as_view(), name='edit-avatar'),
]

app_name = 'user'
