from django.urls import path
from private_app import views

urlpatterns = [
    path('', views.private_view, name='private'),
    path('terminal', views.terminal_view, name='terminal'),
    path('math', views.math_view, name='math'),
]