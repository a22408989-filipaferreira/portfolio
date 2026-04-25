from django.shortcuts import render

from django.shortcuts import render
from .models import Profile, Project, Skill, Tech, Course


def profile_view(request):
    profile = Profile.objects.first()
    return render(request, 'portfolio/profile.html', {'profile': profile})


def projects_view(request):
    projects = Project.objects.select_related('subject').prefetch_related('techs', 'skills')
    return render(request, 'portfolio/projects.html', {'projects': projects})


def skills_view(request):
    skills = Skill.objects.select_related('profile')
    return render(request, 'portfolio/skills.html', {'skills': skills})


def techs_view(request):
    techs = Tech.objects.all()
    return render(request, 'portfolio/techs.html', {'techs': techs})


def courses_view(request):
    courses = Course.objects.prefetch_related('subjects')
    return render(request, 'portfolio/courses.html', {'courses': courses})