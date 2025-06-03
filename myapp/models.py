from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    code = models.TextField()
    tags = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']