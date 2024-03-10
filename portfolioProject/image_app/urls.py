from django.urls import path
from image_app import views

urlpatterns = [
    path('', views.image_view, name='image-view'),
]