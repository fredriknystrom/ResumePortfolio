from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    created_at = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=forms.fields.datetime.date.today
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'created_at']


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']