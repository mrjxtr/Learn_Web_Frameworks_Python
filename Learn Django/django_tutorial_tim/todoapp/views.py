from django.shortcuts import render, HttpResponsePermanentRedirect
from .models import ToDoList
from .forms import CreateNewList

# Create your views here.


def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if request.method == "POST":
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)) == "checked":
                    item.completed = True
                else:
                    item.completed = False

                item.save()

        elif request.POST.get("addItem"):
            text = request.POST.get("item")

            if len(text) > 2:
                ls.item_set.create(text=text, completed=False)
            else:
                print("invalid")

    return render(request, "todoapp/list.html", {"ls": ls})


def home(request):
    return render(request, "todoapp/index.html", {})


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponsePermanentRedirect("/%i" % t.id)

    else:
        form = CreateNewList()

    return render(request, "todoapp/create.html", {"form": form})
