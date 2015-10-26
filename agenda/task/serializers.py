from rest_framework import serializers
from agenda.tarefas.models import Tarefa

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ('task', 'done')
    
