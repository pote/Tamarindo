from django.db import models

class Task (models.Model):
	name = models.CharField(max_length=200)
	difficulty = models.IntegerField()
	start_date = models.DateTimeField()
	started = models.BooleanField()
	completed = models.BooleanField()
	completion_date = models.DateTimeField()
	


	
	

