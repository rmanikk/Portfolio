from django.db.models import Prefetch
from django.shortcuts import render

from .models import Company, Experience


def experience_list(request):

    experiences = Experience.objects.select_related(
        "company"
    ).prefetch_related(
        "bullets"
    ).order_by(
        "order",
        "-start_date",
    )

    companies = Company.objects.prefetch_related(
        Prefetch(
            "experiences",
            queryset=experiences,
        )
    )

    context = {
        "companies": companies,
        "experience_count": experiences.count(),
    }

    return render(
        request,
        "experience/index.html",
        context,
    )