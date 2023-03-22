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


def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'gantt_chart/task_list.html', context)

@login_required
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



def edit_task(request, task_id):
    #Choose the task you want to edit
    task = Task.objects.get(id=task_id)

    if request.method != "POST":
        form = NewTaskForm(instance=task)
    else: 
        form = NewTaskForm(instance=task, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('gantt_chart:chart')
        
    context = {'task':task, 'form':form}
    return render(request, 'gantt_chart/edit_task.html', context)

def my_tasks(request):
    tasks = Task.objects.filter(responsible = request.user).order_by('end_date')
    context = {'my_tasks':tasks}
    return render(request, 'gantt_chart/my-tasks.html', context)    





    
