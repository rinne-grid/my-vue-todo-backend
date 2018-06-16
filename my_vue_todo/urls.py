from django.urls import path, re_path
from .views import ref_task_list, create_task

urlpatterns = [
    path(r'todo_list', ref_task_list),
    path(r'todo_create', create_task),
]

