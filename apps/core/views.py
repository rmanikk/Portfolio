from django.shortcuts import render

from apps.projects.models import Project
from apps.blog.models import BlogPost


def home(request):

    featured_projects = Project.objects.filter(
        featured=True
    ).order_by("order", "-created_at")[:2]

    featured_blogs = BlogPost.objects.filter(
        featured=True,
        published=True
    ).order_by("-published_at", "-created_at")[:3]

    return render(
        request,
        "home/index.html",
        {
            "featured_projects": featured_projects,
            "featured_blogs": featured_blogs,
        },
    )