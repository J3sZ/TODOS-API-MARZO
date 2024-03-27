from django.db import models

# Create your models here.

class task(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True)

    def __str__(self):
        return self.title