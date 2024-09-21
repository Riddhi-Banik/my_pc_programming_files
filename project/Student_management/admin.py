from django.contrib import admin
from .models import Student

class StudentRecent(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'section', 'gpa', 'photo')

admin.site.register(Student, StudentRecent)