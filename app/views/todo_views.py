from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from ..forms import *
from ..models import *


@require_GET
def todo_list(request):
    todos = Todo.objects.all()
    form = TodoForm()
    return render(request, 'todo/list.html', {'todos':todos, 'form':form})


@require_POST
def todo_create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save()
    return redirect('todo-list')


@require_POST
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo-list')