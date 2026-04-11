import json

from django.core.management.base import BaseCommand
from portfolio.models import Course, CapstoneProject, Tech


class Command(BaseCommand):
    help = "Load TFC data from JSON file"

    def handle(self, *args, **options):
        file_path = "data/dados_tfcs_deisi.json"

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        tfcs = data.get("TFCs_2025", [])

        loaded_count = 0

        for item in tfcs:
            course_name = item.get("licenciatura", "").strip()
            title = item.get("titulo", "").strip()

            if not title or not course_name:
                continue

            course, _ = Course.objects.get_or_create(
                name=course_name,
                defaults={
                    "acronym": "",
                    "degree": "Bachelor",
                    "total_ects": 180,
                    "scientific_area": "",
                    "profile_id": 1,  # ajustar se necessário
                }
            )

            capstone_project, created = CapstoneProject.objects.get_or_create(
                title=title,
                year=int(item.get("ano", "0").strip() or 0),
                course=course,
                defaults={
                    "summary": item.get("sumario", "").strip(),
                    "authors": item.get("autores", "").strip(),
                    "advisors": item.get("orientadores", "").strip(),
                    "email": item.get("email", "").split("\n")[0].strip(),
                    "pdf_url": item.get("pdf", "").strip(),
                    "image_url": item.get("imagem", "").strip(),
                    "keywords": "; ".join(
                        kw.strip().rstrip(".")
                        for kw in item.get("palavras_chave", [])
                        if kw.strip()
                    ),
                    "areas": "; ".join(
                        area.strip().rstrip(".")
                        for area in item.get("areas", [])
                        if area.strip()
                    ),
                    "rating": item.get("rating", 0),
                }
            )

            if created:
                for tech_name in item.get("tecnologias", []):
                    clean_tech = tech_name.strip().rstrip(".")
                    if clean_tech:
                        tech, _ = Tech.objects.get_or_create(name=clean_tech)
                        capstone_project.techs.add(tech)

                loaded_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"{loaded_count} TFC(s) loaded successfully.")
        )