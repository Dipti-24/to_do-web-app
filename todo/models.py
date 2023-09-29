from django.db import models
from django.utils import timezone
 
 
class Todo(models.Model):
    task = models.CharField(max_length=100)
    details = models.TextField()
    due_date = models.DateTimeField(default=timezone.now)
    updated=models.DateField(auto_now=True)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.task