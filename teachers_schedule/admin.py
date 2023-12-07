from django.contrib import admin
from .models import TeacherSchedule

class TeacherScheduleAdmin(admin.ModelAdmin):
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
