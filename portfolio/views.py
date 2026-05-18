from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Project, Skill, Tech, Course, MakingOf
from .forms import ProjectForm, TechForm, SkillForm, CourseForm, MakingOfForm


def profile_view(request):
    profile = Profile.objects.first()
    return render(request, "portfolio/profile.html", {"profile": profile})


def projects_view(request):
    projects = Project.objects.all()
    return render(request, "portfolio/projects.html", {"projects": projects})


def skills_view(request):
    skills = Skill.objects.all()
    return render(request, "portfolio/skills.html", {"skills": skills})


def techs_view(request):
    techs = Tech.objects.all()
    return render(request, "portfolio/techs.html", {"techs": techs})


def courses_view(request):
    courses = Course.objects.all()
    return render(request, "portfolio/courses.html", {"courses": courses})


def project_create(request):
    form = ProjectForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("projects")

    return render(request, "portfolio/form.html", {"form": form, "title": "Criar Projeto"})


def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect("projects")

    return render(request, "portfolio/form.html", {"form": form, "title": "Editar Projeto"})


def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        project.delete()
        return redirect("projects")

    return render(request, "portfolio/confirm_delete.html", {"object": project, "title": "Apagar Projeto"})


def tech_create(request):
    form = TechForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("techs")

    return render(request, "portfolio/form.html", {
        "form": form,
        "title": "Criar Tecnologia",
        "back_url": "techs"
    })


def tech_edit(request, pk):
    tech = get_object_or_404(Tech, pk=pk)
    form = TechForm(request.POST or None, instance=tech)

    if form.is_valid():
        form.save()
        return redirect("techs")

    return render(request, "portfolio/form.html", {
        "form": form,
        "title": "Editar Tecnologia",
        "back_url": "techs"
    })


def tech_delete(request, pk):
    tech = get_object_or_404(Tech, pk=pk)

    if request.method == "POST":
        tech.delete()
        return redirect("techs")

    return render(request, "portfolio/confirm_delete.html", {
        "object": tech,
        "title": "Apagar Tecnologia",
        "back_url": "techs"
    })


def skill_create(request):
    form = SkillForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("skills")

    return render(request, "portfolio/form.html", {
        "form": form,
        "title": "Criar Competência",
        "back_url": "skills"
    })


def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    form = SkillForm(request.POST or None, instance=skill)

    if form.is_valid():
        form.save()
        return redirect("skills")

    return render(request, "portfolio/form.html", {
        "form": form,
        "title": "Editar Competência",
        "back_url": "skills"
    })


def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == "POST":
        skill.delete()
        return redirect("skills")

    return render(request, "portfolio/confirm_delete.html", {
        "object": skill,
        "title": "Apagar Competência",
        "back_url": "skills"
    })


def course_create(request):
    form = CourseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("courses")

    return render(request, "portfolio/form.html", {
        "form": form,
        "title": "Criar Formação",
        "back_url": "courses"
    })


def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)

    if form.is_valid():
        form.save()
        return redirect("courses")

    return render(request, "portfolio/form.html", {
        "form": form,
        "title": "Editar Formação",
        "back_url": "courses"
    })


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        course.delete()
        return redirect("courses")

    return render(request, "portfolio/confirm_delete.html", {
        "object": course,
        "title": "Apagar Formação",
        "back_url": "courses"
    })

def navigation_map_view(request):
    return render(request, "portfolio/navigation_map.html")

def github_view(request):
    return render(request, "portfolio/github.html")

def making_of_view(request):
    entries = MakingOf.objects.all().order_by("-created_at")
    return render(request, "portfolio/making_of.html", {"entries": entries})


def making_of_create(request):
    form = MakingOfForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():
        form.save()
        return redirect("making_of")

    return render(request, "portfolio/form.html", {
        "form": form,
        "title": "Criar Entrada Making-Of",
        "back_url": "making_of"
    })


def making_of_edit(request, pk):
    entry = get_object_or_404(MakingOf, pk=pk)
    form = MakingOfForm(
        request.POST or None,
        request.FILES or None,
        instance=entry
    )

    if form.is_valid():
        form.save()
        return redirect("making_of")

    return render(request, "portfolio/form.html", {
        "form": form,
        "title": "Editar Entrada Making-Of",
        "back_url": "making_of"
    })


def making_of_delete(request, pk):
    entry = get_object_or_404(MakingOf, pk=pk)

    if request.method == "POST":
        entry.delete()
        return redirect("making_of")

    return render(request, "portfolio/confirm_delete.html", {
        "object": entry,
        "title": "Apagar Entrada Making-Of",
        "back_url": "making_of"
    })