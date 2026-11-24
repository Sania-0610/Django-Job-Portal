# from django.contrib import admin
# from .models import Job

# admin.site.register(Job)

# Register your models here.
from django.contrib import admin
from .models import Application, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "salary")
    list_filter = ("location", "company")
    search_fields = ("title", "company", "location")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("applicant_name", "email", "job", "applied_at")
    list_filter = ("job",)
    search_fields = ("applicant_name", "email")