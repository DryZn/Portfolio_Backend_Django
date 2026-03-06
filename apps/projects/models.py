from django.db import models


class Project(models.Model):
    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("in_progress", "In Progress"),
        ("planned", "Planned"),
    ]

    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name="Description")
    technologies = models.JSONField(default=list, verbose_name="Technologies")
    github_url = models.URLField(blank=True, verbose_name="GitHub URL")
    demo_url = models.URLField(blank=True, verbose_name="Demo URL")
    image = models.ImageField(upload_to="projects/", blank=True, verbose_name="Image")
    featured = models.BooleanField(default=False, verbose_name="Featured Project")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="completed"
    )
    order = models.IntegerField(default=0, verbose_name="Display Order")
    views = models.IntegerField(default=0, verbose_name="View Count")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title
