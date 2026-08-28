from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)

    logo = models.ImageField(
        upload_to="companies/",
        blank=True,
        null=True,
    )

    website = models.URLField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Experience(models.Model):

    EMPLOYMENT_TYPES = [
        ("full-time", "Full-time"),
        ("part-time", "Part-time"),
        ("internship", "Internship"),
        ("freelance", "Freelance"),
        ("contract", "Contract"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="experiences",
    )

    position = models.CharField(
        max_length=200,
    )

    employment_type = models.CharField(
        max_length=50,
        choices=EMPLOYMENT_TYPES,
        default="full-time",
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True,
    )

    currently_working = models.BooleanField(
        default=False,
    )

    technologies = models.JSONField(
        default=list,
        blank=True,
    )

    featured = models.BooleanField(
        default=False,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["order", "-start_date"]

    def save(self, *args, **kwargs):
        # Only one experience can be featured.
        if self.featured:
            Experience.objects.filter(
                featured=True
            ).exclude(
                pk=self.pk
            ).update(
                featured=False
            )

        # If this is the current job, there is no end date.
        if self.currently_working:
            self.end_date = None

        super().save(*args, **kwargs)

    @property
    def duration(self):
        """
        Returns a simple duration such as:
        5m, 1y 2m, etc.
        """
        from dateutil.relativedelta import relativedelta
        from django.utils import timezone

        end = (
            timezone.now().date()
            if self.currently_working
            else self.end_date
        )

        if not end:
            return ""

        difference = relativedelta(
            end,
            self.start_date,
        )

        years = difference.years
        months = difference.months

        if years and months:
            return f"{years}y {months}m"

        if years:
            return f"{years}y"

        return f"{months}m"

    def __str__(self):
        return f"{self.position} at {self.company.name}"


class ExperienceBullet(models.Model):

    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE,
        related_name="bullets",
    )

    description = models.TextField()

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.description[:60]