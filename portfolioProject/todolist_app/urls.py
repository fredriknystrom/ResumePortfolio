from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('<uuid:task_id>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('update/<uuid:task_id>/', views.UpdateTaskView.as_view(), name='task_update'),
    path('delete/<uuid:task_id>/', views.DeleteTaskView.as_view(), name='task_delete')
]
