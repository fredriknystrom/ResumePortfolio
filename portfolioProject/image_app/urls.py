from django.urls import path
from image_app import views

urlpatterns = [
    path('', views.upload_image, name='mnist-view'),
]