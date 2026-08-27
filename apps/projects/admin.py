from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "featured",
        "order",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "featured",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "order",
        "-created_at",
    )

    fieldsets = (
        (
            "Project Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "short_description",
                    "description",
                    "image",
                )
            },
        ),
        (
            "Project Links",
            {
                "fields": (
                    "github_url",
                    "live_url",
                )
            },
        ),
        (
            "Technologies",
            {
                "fields": (
                    "technologies",
                ),
                "description": (
                    'Enter technologies as JSON. Example: '
                    '["Django", "PostgreSQL", "JavaScript"]'
                ),
            },
        ),
        (
            "Homepage",
            {
                "fields": (
                    "featured",
                    "order",
                )
            },
        ),
    )