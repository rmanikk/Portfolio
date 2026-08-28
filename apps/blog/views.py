from django.shortcuts import get_object_or_404, render

from .models import BlogPost


def blog_list(request):
    posts = BlogPost.objects.filter(
        published=True
    ).order_by(
        "-published_at",
        "-created_at",
    )

    return render(
        request,
        "blog/index.html",
        {
            "posts": posts,
        },
    )


def blog_detail(request, slug):
    post = get_object_or_404(
        BlogPost,
        slug=slug,
        published=True,
    )

    other_posts = (
        BlogPost.objects
        .filter(published=True)
        .exclude(pk=post.pk)
        .order_by("-published_at", "-created_at")[:2]
    )

    return render(
        request,
        "blog/detail.html",
        {
            "post": post,
            "other_posts": other_posts,
        },
    )