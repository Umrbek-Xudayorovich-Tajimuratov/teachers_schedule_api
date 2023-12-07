from django.db import models

# Create your models here.
class TeacherSchedule(models.Model):
    teacher_name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Teacher Schedule"
        verbose_name_plural = "Teacher Schedules"
        ordering = ("group", "teacher_name")