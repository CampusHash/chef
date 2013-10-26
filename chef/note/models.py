from django.contrib.auth.models import User
from django.db import models

class Note(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return  self.title
