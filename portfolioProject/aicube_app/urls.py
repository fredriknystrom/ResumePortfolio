from django.urls import path
from aicube_app import views

urlpatterns = [
    path('', views.ai_cube_view, name='ai-cube'),
]