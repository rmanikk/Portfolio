from django.shortcuts import get_object_or_404, render

from .models import Project


def project_list(request):
    projects = Project.objects.all()

    context = {
        "projects": projects,
    }

    return render(
        request,
        "projects/index.html",
        context,
    )


def project_detail(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug,
    )

    context = {
        "project": project,
    }

    return render(
        request,
        "projects/detail.html",
        context,
    )