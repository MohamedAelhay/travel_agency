from django.db import models
from users.models import CustomUser
from places.models import City
# Create your models here.


class Post(models.Model):
    post_Text = models.CharField(max_length=500)
    post_Created_at = models.DateTimeField(auto_now_add=True)
    post_Updated_at = models.DateTimeField(auto_now=True)
    user_Name = models.ForeignKey(CustomUser)
    city_Name = models.ForeignKey(City)

    class Meta:
        verbose_name_plural = "Posts"


class Comment(models.Model):
    comment_Text = models.CharField(max_length=500)
    comment_Created_at = models.DateTimeField(auto_now_add=True)
    comment_Updated_at = models.DateTimeField(auto_now=True)
    user_Name = models.ForeignKey(CustomUser)
    post_Id = models.ForeignKey(Post)

    class Meta:
        verbose_name_plural = "Comments"



