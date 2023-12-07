from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import TodoForm, UpdateForm
from .models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todo_app/list.html"
    context_object_name = "todo_list"
    paginate_by = 3


class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo_app/create.html"
    form_class = TodoForm
    success_url = reverse_lazy('main')


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "todo_app/update.html"
    form_class = UpdateForm
    success_url = reverse_lazy('main')


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo_app/delete.html"
    success_url = reverse_lazy('main')
