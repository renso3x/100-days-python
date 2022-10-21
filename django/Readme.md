## Installation Setup

> virtualenv venv
> pip install django

## Python shell SQL

> python manage.py shell

```
from main.models import TodoList, Item

t = TodoList(name="test")
t.save()

# Get todos
TodoList.objects.all()

t.item_set.create(text="class")
# Get item
t.item_set.all()

```
