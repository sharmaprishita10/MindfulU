from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("id" , "username", "email")

class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id" , "title")

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id" , "title", "duration")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id" , "user", "program", "comment", "comment_date")

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Comment, CommentAdmin)