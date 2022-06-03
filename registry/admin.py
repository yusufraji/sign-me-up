from django.contrib import admin

from .models import Faculty, Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "faculty"]
    search_fields = ["name", "phone", "email"]


admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty)
