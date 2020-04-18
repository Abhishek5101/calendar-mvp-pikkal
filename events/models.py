from django.db import models


class Event(models.Model):
	event_title = models.CharField(max_length=250)
	event_date = models.DateField()
	event_type = models.CharField(max_length=250)
	
	def __str__(self):
		return f'{self.event_title} on {self.event_date}'
