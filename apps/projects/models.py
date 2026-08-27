from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/"
    )

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    technologies = models.JSONField(
        default=list,
        blank=True
    )

    featured = models.BooleanField(
        default=False
    )

    order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["order", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title