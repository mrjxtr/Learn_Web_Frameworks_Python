from django.shortcuts import render
from .models import ToDoList

# Create your views here.

def index(request, id):
    ls = ToDoList.objects.get(id=id)
    return render(request, 'todoapp/list.html', {"ls":ls})

def home(request):
    return render(request, 'todoapp/index.html', {})
