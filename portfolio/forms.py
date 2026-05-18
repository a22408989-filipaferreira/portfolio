from django import forms
from .models import Project, Tech, Skill, Course, TechType, MakingOf


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class TechForm(forms.ModelForm):
    class Meta:
        model = Tech
        fields = "__all__"


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class TechTypeForm(forms.ModelForm):
    class Meta:
        model = TechType
        fields = "__all__"


class MakingOfForm(forms.ModelForm):
    class Meta:
        model = MakingOf
        fields = "__all__"