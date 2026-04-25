from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects_view, name='projects'),
    path('skills/', views.skills_view, name='skills'),
    path('techs/', views.techs_view, name='techs'),
    path('courses/', views.courses_view, name='courses'),

    # base route
    path('', views.profile_view, name='profile'),
]