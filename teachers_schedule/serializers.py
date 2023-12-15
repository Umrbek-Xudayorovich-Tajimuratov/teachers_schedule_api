from rest_framework import serializers
from .models import TeacherSchedule

class MyDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherSchedule
        fields = "__all__"
