from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username #username comes from the built-in User model


class Post(models.Model):
    author = models.ForeignKey(User ,on_delete = models.CASCADE, blank = True, null = True)
    title = models.CharField(max_length = 30)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'post-images', blank = True, null = True)

    def __str__(self):
        return self.title