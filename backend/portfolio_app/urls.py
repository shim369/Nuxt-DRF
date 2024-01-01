from django.urls import path

from . import views

urlpatterns = [
    path('newest/', views.NewestProjectsView.as_view()),
]