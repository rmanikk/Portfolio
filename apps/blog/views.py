from django.shortcuts import get_object_or_404, render

from .models import BlogPost


def blog_list(request):
    posts = BlogPost.objects.filter(
        published=True
    )

    featured_post = posts.filter(
        featured=True
    ).first()

    regular_posts = posts.exclude(
        pk=featured_post.pk
    ) if featured_post else posts

    return render(
        request,
        "blog/index.html",
        {
            "featured_post": featured_post,
            "posts": regular_posts,
        },
    )


def blog_detail(request, slug):
    post = get_object_or_404(
        BlogPost,
        slug=slug,
        published=True,
    )

    return render(
        request,
        "blog/detail.html",
        {
            "post": post,
        },
    )