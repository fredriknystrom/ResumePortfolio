from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description']  # Define the fields you want to include in the form
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

class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'todolist_app/task_update.html'
    context_object_name = 'task'
    fields = '__all__'  # Update this to a custom class later cherry picking visual attr
    success_url = reverse_lazy('task_list')

    def get_object(self, queryset=None):
        queryset = Task.objects.all()  # You might want to filter this queryset
        return queryset.get(id=self.kwargs['task_id'])
    
    def get_initial(self):
        initial = super().get_initial()
        task = self.get_object()
        initial["title"] = task.title
        initial["description"] = task.description
        print(initial)
        return initial

class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'todolist_app/task_confirm_delete.html'

    def get_object(self, queryset=None):
        queryset = Task.objects.all()
        return queryset.get(id=self.kwargs['task_id'])
