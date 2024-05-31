from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'status']  # Define the fields you want to include in the form
    success_url = reverse_lazy('task_list')  # Specify the URL to redirect after creating a task
    template_name = 'todolist_app/task_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = Task
    template_name = 'todolist_app/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class TaskDetailView(DetailView):
    model = Task
    template_name = 'todolist_app/task_detail.html'
    context_object_name = 'task'

    def get_object(self, queryset=None):
        queryset = Task.objects.all()
        return queryset.get(id=self.kwargs['task_id'])

@method_decorator(login_required, name='dispatch')
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
  
@method_decorator(login_required, name='dispatch')
class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'todolist_app/task_confirm_delete.html'

    def get_object(self, queryset=None):
        queryset = Task.objects.all()
        return queryset.get(id=self.kwargs['task_id'])
