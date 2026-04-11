from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile
from .models import Skill
from .models import Course
from .models import Teacher
from .models import Tech
from .models import Subject
from .models import Project
from .models import Certification
from .models import WorkExperience
from .models import CapstoneProject
from .models import MakingOf

# PROFILE
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "location")
    search_fields = ("name", "email", "location")


# SKILL
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "skill_type", "level", "profile")
    list_filter = ("skill_type", "level", "profile")
    search_fields = ("name", "description", "skill_type", "profile__name")


# COURSE
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "acronym", "degree", "total_ects", "profile")
    list_filter = ("degree", "profile")
    search_fields = ("name", "acronym", "degree", "scientific_area", "profile__name")


# TEACHER
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "department")
    list_filter = ("department",)
    search_fields = ("name", "email", "department")


# TECH
@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "website")
    list_filter = ("category",)
    search_fields = ("name", "description", "category")


# SUBJECT
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "acronym", "course", "year", "semester", "ects")
    list_filter = ("course", "year", "semester")
    search_fields = ("name", "acronym", "description", "course__name")
    filter_horizontal = ("teachers", "techs")


# PROJECT
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "start_date", "end_date")
    list_filter = ("subject", "start_date", "end_date")
    search_fields = ("title", "description", "concepts", "subject__name")
    filter_horizontal = ("techs", "skills")


# CERTIFICATION
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "institution", "start_date", "end_date", "profile")
    list_filter = ("institution", "start_date", "end_date", "profile")
    search_fields = ("title", "institution", "cert_type", "profile__name")
    filter_horizontal = ("skills",)


# WORK EXPERIENCE
@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ("company", "role", "start_date", "end_date", "is_current", "profile")
    list_filter = ("is_current", "start_date", "end_date", "profile")
    search_fields = ("company", "role", "description", "location", "profile__name")
    filter_horizontal = ("techs", "skills")


# CAPSTONE PROJECT
@admin.register(CapstoneProject)
class CapstoneProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "year", "area")
    list_filter = ("course", "year", "area")
    search_fields = ("title", "summary", "authors", "keywords", "area", "course__name")
    filter_horizontal = ("teachers", "techs")


# MAKING OF
@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("version", "project", "subject", "created_at")
    list_filter = ("created_at", "project", "subject")
    search_fields = ("version", "decisions", "corrections", "justification", "alt_text")