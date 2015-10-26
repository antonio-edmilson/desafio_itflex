from django.contrib import admin
from agenda.tarefas.models import Tarefa

class Tarefa_Admin(admin.ModelAdmin):
    list_display = ("task", "done")
    ordering = ["task"]
    search_fields = ("task", "done")
    list_filter = ("task",)
admin.site.register(Tarefa,Tarefa_Admin)

