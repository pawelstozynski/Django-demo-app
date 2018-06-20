from django.db import models
from django.utils import timezone

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "id={0}, name='{1}', content='{2}', create_date='{3}'".format(self.id, self.name, self.content, self.create_date)


class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=100)