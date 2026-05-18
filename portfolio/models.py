from django.db import models

# Create your models here.

# PROFILE MODEL
class Profile(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.TextField()
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# SKILL MODEL
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    skill_type = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    def __str__(self):
        return self.name

# COURSE MODEL (=> licenciatura)
class Course(models.Model):
    name = models.CharField(max_length=150)
    acronym = models.CharField(max_length=20, blank=True, null=True)
    degree = models.CharField(max_length=100)
    total_ects = models.IntegerField()
    website = models.URLField(blank=True, null=True)
    scientific_area = models.CharField(max_length=100, blank=True, null=True)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    def __str__(self):
        return self.name

# TEACHER MODEL
class Teacher(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to="teachers/", blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class TechType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# TECH MODEL
class Tech(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="tech/", blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tech_type = models.ForeignKey(
        TechType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="techs"
    )

    def __str__(self):
        return self.name

# SUBJECT MODEL (=> unidade curricular)
class Subject(models.Model):
    name = models.CharField(max_length=150)
    acronym = models.CharField(max_length=20, blank=True, null=True)
    ects = models.IntegerField()
    year = models.IntegerField()
    semester = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    syllabus_url = models.URLField(blank=True, null=True)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subjects"
    )
    teachers = models.ManyToManyField(
        Teacher,
        related_name="subjects",
        blank=True
    )
    techs = models.ManyToManyField(
        Tech,
        related_name="subjects",
        blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.course.name})"

# PROJECT MODEL
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    concepts = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    repository_url = models.URLField(blank=True, null=True)
    video_demo_url = models.URLField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="projects"
    )
    techs = models.ManyToManyField(
        Tech,
        related_name="projects",
        blank=True
    )
    skills = models.ManyToManyField(
        Skill,
        related_name="projects",
        blank=True
    )

    def __str__(self):
        return self.title

# CERTIFICATION MODEL
class Certification(models.Model):
    title = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    cert_type = models.CharField(max_length=100, blank=True, null=True)

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="certifications"
    )
    skills = models.ManyToManyField(
        Skill,
        related_name="certifications",
        blank=True
    )

    def __str__(self):
        return self.title

# WORK EXPERIENCE MODEL
class WorkExperience(models.Model):
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    is_current = models.BooleanField(default=False)

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="work_experiences"
    )
    techs = models.ManyToManyField(
        Tech,
        related_name="work_experiences",
        blank=True
    )
    skills = models.ManyToManyField(
        Skill,
        related_name="work_experiences",
        blank=True
    )

    def __str__(self):
        return f"{self.role} @ {self.company}"

# CAPSTONE PROJECT MODEL (=> TFC)
class CapstoneProject(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    authors = models.CharField(max_length=255, blank=True, null=True)
    teachers = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    pdf_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    areas = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="capstone_projects"
    )
    techs = models.ManyToManyField(
        Tech,
        related_name="capstone_projects",
        blank=True
    )

    def __str__(self):
        return self.title

# MAKING OF MODEL
class MakingOf(models.Model):
    version = models.CharField(max_length=50)
    decisions = models.TextField()
    corrections = models.TextField()
    justification = models.TextField()
    notebook_photo = models.ImageField(upload_to="making_of/", blank=True, null=True)
    alt_text = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="making_of_entries",
        blank=True,
        null=True
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="making_of_entries",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Making Of - {self.version}"