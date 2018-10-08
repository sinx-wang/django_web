from django.db import models


# Create your models here.
# 类别
class Category(models.Model):
    name = models.CharField(max_length=100)


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)


# 文章
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
