from django.urls import path
from aicube_app import views

urlpatterns = [
    path('', views.ai_cube_view, name='ai-cube'),
    path('foundations-of-ai', views.ai_view, name='ai-view'),
    path('machine-learning', views.ml_view, name='ml-view'),
    path('neural-networks', views.nn_view, name='nn-view'),
    path('natural-language-processing', views.nlp_view, name='nlp-view'),
    path('computer-vision', views.cv_view, name='cv-view'),
    path('large-language-models', views.rob_view, name='llm-view'),
]