from django.shortcuts import get_object_or_404, render

from .models import BlogPost, Category, Tag


def blog_list(request):

    posts = (
        BlogPost.objects
        .filter(published=True)
        .select_related("category")
        .prefetch_related("tags")
        .order_by(
            "-published_at",
            "-created_at",
        )
    )

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(
        request,
        "blog/index.html",
        {
            "posts": posts,
            "categories": categories,
            "tags": tags,
        },
    )


def blog_detail(request, slug):

    post = get_object_or_404(
        BlogPost.objects
        .select_related("category")
        .prefetch_related("tags"),
        slug=slug,
        published=True,
    )

    other_posts = (
        BlogPost.objects
        .filter(published=True)
        .exclude(pk=post.pk)
        .select_related("category")
        .prefetch_related("tags")
        .order_by(
            "-published_at",
            "-created_at",
        )[:2]
    )

    return render(
        request,
        "blog/detail.html",
        {
            "post": post,
            "other_posts": other_posts,
        },
    )


def category_posts(request, slug):

    category = get_object_or_404(
        Category,
        slug=slug,
    )

    posts = (
        BlogPost.objects
        .filter(
            published=True,
            category=category,
        )
        .select_related("category")
        .prefetch_related("tags")
        .order_by(
            "-published_at",
            "-created_at",
        )
    )

    return render(
        request,
        "blog/index.html",
        {
            "posts": posts,
            "categories": Category.objects.all(),
            "tags": Tag.objects.all(),
            "active_category": category,
        },
    )


def tag_posts(request, slug):

    tag = get_object_or_404(
        Tag,
        slug=slug,
    )

    posts = (
        BlogPost.objects
        .filter(
            published=True,
            tags=tag,
        )
        .select_related("category")
        .prefetch_related("tags")
        .order_by(
            "-published_at",
            "-created_at",
        )
    )

    return render(
        request,
        "blog/index.html",
        {
            "posts": posts,
            "categories": Category.objects.all(),
            "tags": Tag.objects.all(),
            "active_tag": tag,
        },
    )