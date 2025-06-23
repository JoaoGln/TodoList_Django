from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    """
    View para listar todas as tarefas e adicionar novas tarefas.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'tasks/task_list.html', context)

def task_update(request, pk):
    """
    View para editar e atualizar uma tarefa existente.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task
    }
    return render(request, 'tasks/task_update.html', context)

def task_delete(request, pk):
    """
    View para deletar uma tarefa.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    context = {
        'task': task
    }
    return render(request, 'tasks/task_confirm_delete.html', context)