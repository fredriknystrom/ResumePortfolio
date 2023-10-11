from django.urls import path
from resume_app import views

urlpatterns = [
    path('', views.resume_view, name='resume-view'),
]