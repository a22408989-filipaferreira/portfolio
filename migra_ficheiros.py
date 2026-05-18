import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.core.files import File
from portfolio.models import Profile, Project, MakingOf
from artigos.models import Article


def migrate_file(obj, field_name):
    field = getattr(obj, field_name)

    if field and field.name:
        try:
            local_path = field.path
        except Exception:
            print(f"Ignorado, já parece estar na cloud: {obj}")
            return

        if os.path.exists(local_path):
            with open(local_path, "rb") as f:
                field.save(
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )

            print(f"Migrado: {obj}")


for obj in Profile.objects.all():
    migrate_file(obj, "photo")

for obj in Project.objects.all():
    migrate_file(obj, "image")

for obj in MakingOf.objects.all():
    migrate_file(obj, "notebook_photo")

for obj in Article.objects.all():
    migrate_file(obj, "image")