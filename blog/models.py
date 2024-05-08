from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, max_length=250, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
