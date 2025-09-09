from django.urls import path
from .views import cheese_and_mouse

urlpatterns = [
    path('', cheese_and_mouse, name='cheese_and_mouse'),
]