from django.db import models
from django.template.defaultfilters import truncatechars
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from myBlog.utils import unique_slug_generator
from django.utils import timezone

from django.urls import reverse

# I should have created an extended User model.


class Category(models.Model):
    category_name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=199, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='post_likes', null=True, blank=True)

    def __str__(self):
        return truncatechars(self.text, 15)


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return truncatechars(self.text, 15)


# I am not really using slug. These are here just for future reference.
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Category)


class Follow(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='user')
    followed_user = models.ManyToManyField(
        User, blank=True, null=True, related_name='followed_user')

    def __str__(self):
        return self.user.username
