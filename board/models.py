from django.db import models
from members.models import Members
from .models import *

class Board(models.Model):
    user = models.ForeignKey(Members, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(default='')
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(Members, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Board, null=True, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default='')
    
    def __str__(self):
        return self.comment