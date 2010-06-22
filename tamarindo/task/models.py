from django.db import models

class Task (models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    started_date = models.DateTimeField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child_set')
    completed = models.BooleanField()
    completed_date = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name