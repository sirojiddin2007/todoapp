from django.shortcuts import render, redirect
from .models import *


def index_view(request):
    context = {
        'todo': Todo.objects.all()
    }
    return render(request, "index.html", context)


def create_task_view(request):
    if request.method == "POST":
        task = request.POST['task']
        Todo.objects.create(
            task=task
        )
        return redirect('index_url')
    return render(request, 'index.html')


def delete_task(request, pk):
    task = Todo.objects.get(pk=pk)
    task.status = 'In Progress'
    task.save()
    return redirect('index_url')


def finished_task(request, pk):
    task = Todo.objects.get(pk=pk)
    task.status = "FINISHED"
    task.save()
    return redirect('index_url')
