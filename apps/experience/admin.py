from django.contrib import admin

from .models import Company, Experience, ExperienceBullet


class ExperienceBulletInline(admin.TabularInline):
    model = ExperienceBullet
    extra = 1
    fields = ("description", "order")
    ordering = ("order",)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "website", "created_at")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "position",
        "company",
        "employment_type",
        "start_date",
        "end_date",
        "currently_working",
        "featured",
        "order",
    )

    list_filter = (
        "employment_type",
        "currently_working",
        "featured",
    )

    search_fields = (
        "position",
        "company__name",
    )

    ordering = ("order", "-start_date")

    list_editable = (
        "featured",
        "order",
    )

    fieldsets = (
        (
            "Position",
            {
                "fields": (
                    "company",
                    "position",
                    "employment_type",
                )
            },
        ),
        (
            "Employment Period",
            {
                "fields": (
                    "start_date",
                    "end_date",
                    "currently_working",
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
                    'Enter technologies as a JSON list, '
                    'for example: ["Django", "Python", "PostgreSQL"]'
                ),
            },
        ),
        (
            "Portfolio",
            {
                "fields": (
                    "featured",
                    "order",
                )
            },
        ),
    )

    inlines = [ExperienceBulletInline]