from django.shortcuts import render, redirect
from .models import Task
import pandas as pd
import plotly.express as px
from plotly.offline import plot
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from .forms import NewTaskForm

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"



@login_required
def chart(request):
    qs = Task.objects.all()

    #data about each task
    tasks_data = [
        {
        'Name': x.name,
        'Responsible': x.responsible,
        'Start_date': x.start_date,
        'End_date': x.end_date,
        'Weeks_left': x.weeks_left,
        
        } for x in qs
    ]
    #Move data of each task to data frame
    df = pd.DataFrame(tasks_data)

    #plot the Gantt chart
    fig = px.timeline(
        df, x_start='Start_date', x_end='End_date', y='Name', color='Responsible',
        )
    
    fig.update_yaxes(autorange = "reversed")
    gantt_plot = plot(fig, output_type = 'div')
    
    #data transfered to the html page
    context = {'plot_div': gantt_plot}
    return render(request, 'chart.html', context)


def add_task(request):
    if request.method != 'POST':
        form = NewTaskForm()
    else:
        form = NewTaskForm(data = request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.creator = request.user
            new_task.save()
            return redirect('gantt_chart:chart')
        
    context = {'new_task':form}
    return render(request, 'gantt_chart/add_task.html', context)

""" class NewTask(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'add_task.html'
    success_url = '/schedule/' """

""" def edit_task(request, task_id):
    #Choose the entry you want to edit
    task = Task.objects.get(id=task_id)

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else: 
        form = EntryForm(instance=entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
        
    context = {'entry': entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context) """
    





    
