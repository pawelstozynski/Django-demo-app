from django.db import models
from django.utils import timezone

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.content


class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content