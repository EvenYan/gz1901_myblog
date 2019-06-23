from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    modified_time = models.DateTimeField(auto_now_add=True, null=True)
    excerpt = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.title
