from rest_framework import serializers

from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'skill', 'skill_id', 'title', 'description', 'demo_link', 
            'github_repo', 'content', 'created_at', 'updated_at'
        )