from django.shortcuts import render, redirect
from .models import Task
import pandas as pd
import plotly.express as px
from plotly.offline import plot


# Create your views here.

def index(request):
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
    return render(request, 'index.html', context)


    
