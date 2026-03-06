from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(verbose_name="Excerpt")
    content = models.TextField(verbose_name="Content")
    cover_image = models.ImageField(
        upload_to="blog/", blank=True, verbose_name="Cover Image"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Category"
    )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Tags")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    views = models.IntegerField(default=0, verbose_name="Views")
    published_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Published Date"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
