from django.shortcuts import render
from django.http import HttpResponse

from apps.projects.models import Project
from apps.blog.models import BlogPost
from apps.experience.models import Experience


def home(request):

    featured_projects = Project.objects.filter(
        featured=True
    ).order_by(
        "order",
        "-created_at"
    )[:2]

    featured_blogs = BlogPost.objects.filter(
        featured=True,
        published=True
    ).order_by(
        "-published_at",
        "-created_at"
    )[:2]

    featured_experience = Experience.objects.filter(
        featured=True
    ).select_related(
        "company"
    ).prefetch_related(
        "bullets"
    ).first()

    return render(
        request,
        "home/index.html",
        {
            "featured_projects": featured_projects,
            "featured_blogs": featured_blogs,
            "featured_experience": featured_experience,
        },
    )


def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Disallow: /admin/\n"
        "Disallow: /ckeditor5/\n"
        "Allow: /\n"
        "\n"
        "Sitemap: https://www.manikkafle.com.np/sitemap.xml\n"
    )

    return HttpResponse(
        content,
        content_type="text/plain"
    )