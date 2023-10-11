from django.urls import path
from spotistats_app import views

urlpatterns = [
    path('', views.spotistats_view, name='spotistats_view'),
]