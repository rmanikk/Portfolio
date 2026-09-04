from django.db import migrations, models
import django.db.models.deletion


def convert_categories(apps, schema_editor):
    Category = apps.get_model("blog", "Category")
    BlogPost = apps.get_model("blog", "BlogPost")

    categories = {
        "development": "Development",
        "projects": "Projects",
        "learning": "Learning",
        "ai": "AI",
        "design": "Design",
        "personal": "Personal",
    }

    category_objects = {}

    for slug, name in categories.items():
        category, _ = Category.objects.get_or_create(
            slug=slug,
            defaults={"name": name},
        )
        category_objects[slug] = category

    for post in BlogPost.objects.all():

        old_category = post.old_category

        if old_category in category_objects:
            post.category = category_objects[old_category]
            post.save(update_fields=["category"])


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blogpost_content"),
    ]

    operations = [

        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=120,
                        unique=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
                "ordering": ["name"],
            },
        ),

        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=70,
                        unique=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),

        # Keep the original text values temporarily.
        migrations.RenameField(
            model_name="blogpost",
            old_name="category",
            new_name="old_category",
        ),

        # Create the new ForeignKey.
        migrations.AddField(
            model_name="blogpost",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to="blog.category",
            ),
        ),

        # Convert the old values into Category IDs.
        migrations.RunPython(
            convert_categories,
            migrations.RunPython.noop,
        ),

        # Remove the old text column.
        migrations.RemoveField(
            model_name="blogpost",
            name="old_category",
        ),

        # Add tags.
        migrations.AddField(
            model_name="blogpost",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                related_name="posts",
                to="blog.tag",
            ),
        ),
    ]