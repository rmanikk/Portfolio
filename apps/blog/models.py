from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ("development", "Development"),
        ("projects", "Projects"),
        ("learning", "Learning"),
        ("ai", "AI"),
        ("design", "Design"),
        ("personal", "Personal"),
    ]

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    excerpt = models.TextField(
        max_length=500,
        blank=True
    )

    content = CKEditor5Field(
    "Content",
    config_name="extends",
)

    cover_image = models.ImageField(
        upload_to="blog/covers/",
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="development"
    )

    featured = models.BooleanField(default=False)

    published = models.BooleanField(default=False)

    published_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_at", "-created_at"]