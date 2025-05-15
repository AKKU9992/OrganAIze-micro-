from home.models import PriorityTask
from django import forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = PriorityTask
        fields = ['title', 'description', 'due_date', 'completed', 'priority']