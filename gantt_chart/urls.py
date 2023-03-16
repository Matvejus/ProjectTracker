from django.urls import path
from . import views

app_name = 'gantt_chart'
urlpatterns = [
    path('', views.index, name = 'index')
]
