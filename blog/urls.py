from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index),
    # Post Urls:-
    url(r'^posts/$', views.getAllPosts),
    url(r'^(?P<postId>[0-9]+)/$', views.getPostById),
    # Comment Urls:-
    url(r'^comments/$', views.getAllComments),
    url(r'^(?P<commentId>[0-9]+)/$', views.getCommentById),
]



