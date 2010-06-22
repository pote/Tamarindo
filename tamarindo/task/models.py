from django.db import models

class Task (models.Model):
    name = models.CharField(max_length=256)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child_set')    
    description = models.TextField()
    deadline = models.DateTimeField(blank=True, null=True)
    started_date = models.DateTimeField()
    completed = models.BooleanField()
    completed_date = models.DateTimeField(blank=True, null=True)
    
    
    def __unicode__(self):
        return self.name