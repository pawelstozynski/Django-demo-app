from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from ..forms import *
from ..models import *

def todo_list(request):
    todos = Todo.objects.all()
    form = TodoForm()
    return render(request, 'todo/list.html', {'todos':todos, 'form':form})


def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todo-list')
    else:
        return HttpResponse('Not allowed')


def todo_delete(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return redirect('todo-list')
    else:
        return HttpResponse('Not allowed')