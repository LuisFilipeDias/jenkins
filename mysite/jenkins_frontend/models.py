from django.db import models


# Create your models here.

class Post(models.Model):
    job = models.CharField(max_length=140)
    status = models.CharField(max_length=140)
    added = models.DateTimeField()

    def __str__(self):
        return self.job
