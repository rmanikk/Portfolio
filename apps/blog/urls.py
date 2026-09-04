from django.urls import path

from . import views


app_name = "blog"


urlpatterns = [

    path(
        "",
        views.blog_list,
        name="list",
    ),

    path(
        "category/<slug:slug>/",
        views.category_posts,
        name="category",
    ),

    path(
        "tag/<slug:slug>/",
        views.tag_posts,
        name="tag",
    ),

    path(
        "<slug:slug>/",
        views.blog_detail,
        name="detail",
    ),
]