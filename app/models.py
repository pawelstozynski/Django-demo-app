from django.db import models
from django.utils import timezone

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
