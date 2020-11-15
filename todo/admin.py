from django.contrib import admin
from .models import TodoList


# Register your models here.


class TodoListAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoList, TodoListAdmin)
