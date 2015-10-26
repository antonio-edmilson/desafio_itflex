from django.db import models

class Tarefa(models.Model):
    task = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
