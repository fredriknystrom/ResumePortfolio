from django.urls import path, include
from todolist_app import views
from django.views.generic import TemplateView # useful in displaying index.html template

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('<uuid:task_id>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('update/<uuid:task_id>/', views.UpdateTaskView.as_view(), name='task_update'),
    path('delete/<uuid:task_id>/', views.DeleteTaskView.as_view(), name='task_delete')
]
