from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    text_muallif = models.CharField(max_length=80)
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

2