from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='task-index'),
    path('tarefas-pendentes/', views.tasks_pending, name='task-pending'),
    path('criar-tarefa/', views.create_task, name='task-create'),
]
