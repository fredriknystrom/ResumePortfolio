from django.urls import path
from MNIST_app import views

urlpatterns = [
    path('', views.mnist_view, name='mnist-view'),
]