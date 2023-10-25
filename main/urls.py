from django.urls import *
from .views import *

urlpatterns = [
    path('', index_view, name="index_url"),
    path('task-create/', create_task_view, name="create_todo_url"),
    path('task-delete/<int:pk>/', delete_task, name="delete_todo_url"),
    path('task-finished/<int:pk>/', finished_task, name="finished_todo_url"),
]