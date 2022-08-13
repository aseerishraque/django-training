from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class PostCategory(models.Model):
    title = models.CharField(max_length=500, unique=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:20]


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=500)
    body = models.TextField(null=True, blank=True, )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='draft')
    review_status = models.BooleanField(default=True)
    rating = models.ManyToManyField(PostCategory, related_name='post_post_category', blank=True)

    class Meta:
        ordering = ("-publish",)

    def get_absolute_url(self):
        return reverse("blog:post_details", args=(self.id,))

    def __str__(self):
        return self.title[:20]
