from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [

    path("admin/", admin.site.urls),

    path("blog/", include("apps.blog.urls")),

    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path(
    "contact/",
    include("apps.contact.urls"),
),

    path(
        "",
        include("apps.core.urls")
    ),

    path(
        "projects/",
        include("apps.projects.urls")
    ),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )