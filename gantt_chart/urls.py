from django.urls import path
from . import views
from .views import Index

app_name = 'gantt_chart'
urlpatterns = [
    path('schedule/', views.chart, name = 'chart'),
    path("", Index.as_view(), name = "index"),
    path('new-task/', views.add_task, name = "add_task"),
    path('edit-task/<int:task_id>/', views.edit_task, name ="edit_task"),
    path('tasks/', views.task_list, name = "task_list"),
]
