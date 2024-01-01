from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project, Skill
from .serializers import ProjectSerializer

class NewestProjectsView(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()[0:4]
        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)