from rest_framework import serializers
from core.models import Mentor


class MentorSerializer(serializers.ModelSerializer):
    skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = Mentor
        fields = ('id', 'name', 'skills')
