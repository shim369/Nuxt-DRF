from django.forms import ModelForm

from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            'skill', 'title', 'description', 'image_url', 'demo_link',
            'github_repo',
        )