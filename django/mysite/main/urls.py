from django.urls import path
from .views import index, view_todo

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>', view_todo, name="view todo")
]
