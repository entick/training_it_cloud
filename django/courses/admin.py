from django.contrib import admin

from .models import Course, Lesson

# Register your models here.

class LessonInLine(admin.StackedInline):
    model = Lesson
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name']}),
        ('Information',{'fields':['short_description']}),
        ('Coaches',{'fields':['coach','assistant']})
    ]
    inlines = [LessonInLine]
    list_display = ('name','short_description')
    search_fields = ['name']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
