from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="In Progress")

    def str(self):
        return self.task