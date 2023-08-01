from django.shortcuts import render, redirect
from .models import Todo, DeletedTodo
from .forms import TodoForm
from django.contrib import messages
from datetime import datetime


def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            todos = Todo.objects.all()
            deleted_todos = DeletedTodo.objects.all()  # Add this line
            messages.success(request, ('Task has been added!'))
            return render(request, 'home.html', {'todos': todos, 'deleted_todos': deleted_todos})  # Update this line
    else:
        todos = Todo.objects.all()
        deleted_todos = DeletedTodo.objects.all()  # Add this line
        return render(request, 'home.html', {'todos': todos, 'deleted_todos': deleted_todos})  # Update this line


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    deleted_todo = DeletedTodo(task=todo.task)
    deleted_todo.save()
    todo.delete()
    messages.success(request, ('Task has been Deleted!'))
    return redirect('/')

def mark_complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.completion_date = datetime.now()
    todo.save()
    return redirect('/')


def mark_incomplete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.completion_date = None
    todo.save()
    return redirect('/')

def restore(request, todo_id):
    deleted_todo = DeletedTodo.objects.get(id=todo_id)
    todo = Todo()
    todo.task = deleted_todo.task
    todo.save()
    deleted_todo.delete()
    return redirect('/')