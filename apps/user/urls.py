from django.conf.urls import url
from user.views import LoginView, RegisterView, EditView, EditAvatarView

urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^register/$', RegisterView.as_view()),

    url(r'^edit/$', EditView.as_view()),
    url(r'^edit/avatar/$', EditAvatarView.as_view()),
]

app_name = 'user'
