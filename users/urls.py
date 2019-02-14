from django.conf.urls import url
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout' ),
    url(r'^signup/$', views.signup_view, name='signup'),
]