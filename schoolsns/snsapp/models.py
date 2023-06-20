from django.db import models

class Post(models.Model):
    content = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
