from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=45)
    director = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)