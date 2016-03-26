from django.db import models


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=140)
    email = models.CharField(max_length=140)
    added = models.DateTimeField()

    def __str__(self):
        return self.name
