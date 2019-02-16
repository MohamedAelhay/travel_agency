from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello BLOG</h1>")


# Post Methods :-
def getAllPosts(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "postsPage.html", context)


def getPostById(request, postId):
    post = Post.objects.get(id=eval(postId))
    context = {"post": post}
    return render(request, "postPage.html", context)


# Comments Methods :-
def getAllComments(request):
    comments = Comment.objects.all()
    context = {"comments": comments}
    return render(request, "commentsPage.html", context)


def getCommentById(request, commentId):
    comment = Comment.objects.get(id=eval(commentId))
    context = {"comment": comment}
    return render(request, "postPage.html", context)





