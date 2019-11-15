from django.db import models
from django.utils import timezone

class GhostPost(models.Model):
    ghostTitle = models.CharField(max_length=50)
    body = models.TextField(max_length=280)
    is_boast = models.BooleanField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.ghostTitle} - {self.ghostAuthor.name}"