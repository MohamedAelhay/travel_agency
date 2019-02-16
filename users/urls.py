from django.conf.urls import url
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^(?P<student_id>[0-9]+)/$', views.get_user),
    # url(r'^(?P<student_id>[0-9]+)/edit$', views.edit),
    # url(r'^(?P<student_id>[0-9]+)/delete$', views.delete),
    # url(r'^home/$', views.get_all_users),
    # url(r'^new', views.new)
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.signup_view, name='signup'),
]
