from django.shortcuts import render, get_object_or_404, render_to_response
from agenda.tarefas.models import Tarefa

def index(request):
    return render_to_response('tarefas/index.html')