from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^(?P<student_id>[0-9]+)/$', views.get_user),
    # url(r'^(?P<student_id>[0-9]+)/edit$', views.edit),
    # url(r'^(?P<student_id>[0-9]+)/delete$', views.delete),
    # url(r'^home/$', views.get_all_users),
    # url(r'^new', views.new)
]