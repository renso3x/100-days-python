from django.http import HttpResponse
from .models import TodoList, Item

def index(request):
    return HttpResponse("Hello world")

def view_todo(request, id):
    ls = TodoList.objects.get(id=id)
    items = ls.item_set.get(id=1)
    return HttpResponse(f"{id} todo {ls.name}, {items}")
