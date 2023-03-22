from django import forms
from .models import Task

class DateInput(forms.DateInput):
    input_type = 'date'

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'responsible', 'start_date', 'end_date']
        widgets = {
            'start_date':DateInput(),
            'end_date':DateInput(),
        }
