from django.contrib.sitemaps.views import sitemap, index
from apps.core.sitemaps import StaticViewSitemap
from apps.core.views import robots_txt

from apps.blog.sitemaps import BlogPostSitemap
from apps.projects.sitemaps import ProjectSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogPostSitemap,
    "projects": ProjectSitemap,
}


urlpatterns = [

    

    path("admin/", admin.site.urls),

    path(
    "sitemap.xml",
    sitemap,
    {"sitemaps": sitemaps},
    name="sitemap",
),
path(
    "robots.txt",
    robots_txt,
    name="robots_txt",
),

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
    path(
    "experience/",
    include("apps.experience.urls")
),

]