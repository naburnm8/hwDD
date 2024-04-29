from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail')
]