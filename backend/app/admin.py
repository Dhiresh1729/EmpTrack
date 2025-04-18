from django.contrib import admin
from .models import Employee, Attendance, Performance, Department, Project

# Register your models here.
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Performance)
admin.site.register(Department)
admin.site.register(Project)
