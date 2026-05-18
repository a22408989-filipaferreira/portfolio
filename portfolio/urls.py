from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile_view, name="profile"),

    path("projects/", views.projects_view, name="projects"),
    path("projects/create/", views.project_create, name="project_create"),
    path("projects/<int:pk>/edit/", views.project_edit, name="project_edit"),
    path("projects/<int:pk>/delete/", views.project_delete, name="project_delete"),

    path("skills/", views.skills_view, name="skills"),
    path("techs/", views.techs_view, name="techs"),
    path("courses/", views.courses_view, name="courses"),
    
    path("techs/create/", views.tech_create, name="tech_create"),
    path("techs/<int:pk>/edit/", views.tech_edit, name="tech_edit"),
    path("techs/<int:pk>/delete/", views.tech_delete, name="tech_delete"),

    path("skills/create/", views.skill_create, name="skill_create"),
    path("skills/<int:pk>/edit/", views.skill_edit, name="skill_edit"),
    path("skills/<int:pk>/delete/", views.skill_delete, name="skill_delete"),

    path("courses/create/", views.course_create, name="course_create"),
    path("courses/<int:pk>/edit/", views.course_edit, name="course_edit"),
    path("courses/<int:pk>/delete/", views.course_delete, name="course_delete"),

    path("navigation-map/", views.navigation_map_view, name="navigation_map"),
    path("github/", views.github_view, name="github"),

    path("making-of/", views.making_of_view, name="making_of"),
    path("making-of/create/", views.making_of_create, name="making_of_create"),
    path("making-of/<int:pk>/edit/", views.making_of_edit, name="making_of_edit"),
    path("making-of/<int:pk>/delete/", views.making_of_delete, name="making_of_delete"),
]