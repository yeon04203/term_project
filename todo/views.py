from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import TodoList
from django.views import generic
from .forms import TodoCreateForm


# Create your views here. 


class IndexView(generic.ListView):
    context_object_name = 'to_do_list'

    def get_queryset(self):
        return TodoList.objects.filter(author=self.request.user)


class DetailView(generic.DetailView):
    contxt_object_name = 'todolist'

    def get_queryset(self):
        return TodoList.objects.filter(author=self.request.user)


class DeleteView(generic.DeleteView):
    success_url = reverse_lazy("todo:todolist")
    tempalte_name = 'todo/delete.html'

    def get_queryset(self):
        return TodoList.objects.filter(author=self.request.user)


class UpdateView(generic.UpdateView):
    fields = ['name', 'description', 'date_deadline']
    template_name = 'todo/create.html'
    success_url = reverse_lazy("todo:todolist")

    def get_queryset(self):
        return TodoList.objects.filter(author=self.request.user)


class CreateView(generic.CreateView):
    form_class = TodoCreateForm
    success_url = reverse_lazy("todo:todolist")
    template_name = "todo/create.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(form)
