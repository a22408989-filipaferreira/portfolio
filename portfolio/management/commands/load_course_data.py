import requests
from django.core.management.base import BaseCommand
from portfolio.models import Profile, Course, Subject


class Command(BaseCommand):
    help = "Load course and curricular units data from Lusofona API"

    def handle(self, *args, **options):
        school_year = "202526"
        course_code = 260  # LEI
        language = "PT"

        headers = {"content-type": "application/json"}

        # because there can't be a course without an associated profile
        profile = Profile.objects.first()

        if not profile:
            profile = Profile.objects.create(
                name="Default Profile",
                bio="Automatically created profile for course loading",
                email="default@example.com",
                location="Lisbon"
            )

        # load course details
        course_url = "https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail"
        course_payload = {
            "language": language,
            "courseCode": course_code,
            "schoolYear": school_year,
        }

        response = requests.post(course_url, json=course_payload, headers=headers)
        response.raise_for_status()
        course_data = response.json()

        # adapt the fields that come from the API
        course_name = course_data.get("name") or course_data.get("courseName") or "Licenciatura em Engenharia Informática"
        course_acronym = course_data.get("acronym") or course_data.get("courseAcronym") or "LEI"
        total_ects = course_data.get("ects") or course_data.get("courseEcts") or 180
        scientific_area = course_data.get("scientificArea") or ""
        website = course_data.get("website") or ""

        course, created = Course.objects.get_or_create(
            name=course_name,
            defaults={
                "acronym": course_acronym,
                "degree": "Bachelor",
                "total_ects": int(total_ects),
                "website": website,
                "scientific_area": scientific_area,
                "profile": profile,
            }
        )

        if not created:
            course.acronym = course_acronym
            course.total_ects = int(total_ects)
            course.website = website
            course.scientific_area = scientific_area
            course.profile = profile
            course.save()

        loaded_subjects = 0

        # load UCs
        for uc in course_data.get("courseFlatPlan", []):
            uc_name = uc.get("curricularUnitName") or uc.get("name") or ""
            uc_code = uc.get("curricularIUnitReadableCode") or uc.get("readableCode") or ""
            uc_ects = uc.get("ects") or 0
            uc_year = uc.get("year")
            uc_semester = uc.get("semester")

            if isinstance(uc_year, int):
                year_value = uc_year
            else:
                text = str(uc_year)

                if "1" in text:
                    year_value = 1
                elif "2" in text:
                    year_value = 2
                elif "3" in text:
                    year_value = 3
                else:
                    year_value = 0

            if isinstance(uc_semester, int):
                semester_value = uc_semester
            else:
                if "1" in str(uc_semester):
                    semester_value = 1
                elif "2" in str(uc_semester):
                    semester_value = 2
                else:
                    semester_value = 0

            if not uc_name:
                continue

            # ask API UCs details
            uc_detail_url = "https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails"
            uc_detail_payload = {
                "language": language,
                "curricularIUnitReadableCode": uc_code,
            }

            uc_response = requests.post(uc_detail_url, json=uc_detail_payload, headers=headers)
            uc_response.raise_for_status()
            uc_detail = uc_response.json()

            description = (
                uc_detail.get("summary")
                or uc_detail.get("syllabus")
                or uc_detail.get("objectives")
                or uc_detail.get("description")
                or ""
            )

            syllabus_url = uc_detail.get("url") or ""

            Subject.objects.update_or_create(
                course=course,
                name=uc_name,
                defaults={
                    "acronym": uc_code,
                    "ects": int(uc_ects),
                    "year": year_value,
                    "semester": semester_value,
                    "description": description,
                    "syllabus_url": syllabus_url,
                }
            )

            loaded_subjects += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Course loaded: {course.name} | Subjects loaded: {loaded_subjects}"
            )
        )