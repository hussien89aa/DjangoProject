from django.contrib import admin

# Register your models here.
from sellingportal.models import Student, Degree

admin.site.register(Student)
admin.site.register(Degree)
