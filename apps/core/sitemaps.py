from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return [
            "home",
            "projects:project_list",
            "blog:list",
            "experience:experience_list",
            "contact:contact",
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == "home":
            return 1.0

        if item in {
            "projects:project_list",
            "blog:list",
        }:
            return 0.9

        return 0.7