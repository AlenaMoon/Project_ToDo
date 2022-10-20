# Create your views here.
from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect
from django.http import HttpResponse
#
#
# def index (request):
#     return HttpResponse("Hello! I start project!")


def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/AppToDo/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/AppToDo/')
    # return HttpResponse("Yes!!! I did it!")