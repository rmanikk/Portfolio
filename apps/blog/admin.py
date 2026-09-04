from django.contrib import admin

from .models import BlogPost, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "featured",
        "published",
        "published_at",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
        "published",
        "tags",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
        "category__name",
        "tags__name",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    filter_horizontal = (
        "tags",
    )

    ordering = (
        "-published_at",
        "-created_at",
    )