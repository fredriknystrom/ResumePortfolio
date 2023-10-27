from django.urls import path
from private_app import views

urlpatterns = [
    path('', views.terminal_view, name='terminal'),
]