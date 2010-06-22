from django.db import models

class Task (models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    completed = models.BooleanField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child_set')
    
    
    def __unicode__(self):
        return self.name