from django.contrib import admin
from .models import Meetings, Teachers, Students, Courses

# Register your models here.
admin.site.register(Meetings)
admin.site.register(Teachers)
admin.site.register(Students)
admin.site.register(Courses)
