from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agenda.tarefas.models import Tarefa
from agenda.task.serializers import TaskSerializer

@api_view(['GET', 'POST'])
def list_task(request):
    
    if request.method == 'GET':
        tasks = Tarefa.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            print "salvei huhuhuhu"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        