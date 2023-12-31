from django.urls import path, include

from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='main'),
    path("todo_app/create", TodoCreateView.as_view(), name="create-todo"),
    path("todo_app/edit/<pk>", TodoUpdateView.as_view(), name="edit-todo"),
    path("todo_app/delete/<pk>", TodoDeleteView.as_view(), name="delete-todo")
]
