from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(blank=True, null=True,  auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task

class DeletedTodo(models.Model):
    task = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
