from django.contrib import admin
from .models import TeacherSchedule
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class TeacherScheduleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('teacher_name', 'group', 'subject')
    search_fields = ('teacher_name__contains','group__contains','subject__contains')
    fieldsets = (
        ('Teacher Informations', {
            'fields': ('teacher_name',)
        }),
        ('Group Details', {
            'classes': ('wide',),
            'fields': ('group', ),
        }),
        ('Subject Details', {
            'classes': ('wide',),
            'fields': ('subject',),
            }),
    )

# Register your models here.
admin.site.register(TeacherSchedule, TeacherScheduleAdmin)
