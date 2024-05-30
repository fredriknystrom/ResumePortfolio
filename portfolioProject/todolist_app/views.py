from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Task
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'status']  # Define the fields you want to include in the form
    success_url = reverse_lazy('task_list')  # Specify the URL to redirect after creating a task
    template_name = 'todolist_app/task_create.html'


class TaskListView(ListView):
    model = Task
    template_name = 'todolist_app/task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todolist_app/task_detail.html'
    context_object_name = 'task'

    def get_object(self, queryset=None):
        queryset = Task.objects.all()
        return queryset.get(id=self.kwargs['task_id'])

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']

class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'todolist_app/task_update.html'
    context_object_name = 'task'
    form_class = TaskUpdateForm
    success_url = reverse_lazy('task_list')

    def get_object(self, queryset=None):
        queryset = Task.objects.all()  # You might want to filter this queryset
        return queryset.get(id=self.kwargs['task_id'])
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        task = self.get_object()
        kwargs['instance'] = task
        return kwargs
  

class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'todolist_app/task_confirm_delete.html'

    def get_object(self, queryset=None):
        queryset = Task.objects.all()
        return queryset.get(id=self.kwargs['task_id'])
