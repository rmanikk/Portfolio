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

    # Pick two other projects for the "Explore More Projects" section.
    recommended_projects = (
        Project.objects
        .exclude(pk=project.pk)
        .order_by("-pk")[:2]
    )

    context = {
        "project": project,
        "recommended_projects": recommended_projects,
    }

    return render(
        request,
        "projects/detail.html",
        context,
    )