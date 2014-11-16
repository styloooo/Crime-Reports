from django.db import models

# Create your models here.
class Crime(models.Model):
	incident_num = models.CharField(max_length=10, primary_key=True)
	incident = models.CharField(max_length=20, blank=True, null=True)
	attempt = models.BooleanField(default=False, blank=True)
	address = models.CharField(max_length=80)
	location_name = models.CharField(max_length=50, null=True, blank=True)
	officer = models.CharField(max_length=30)
	date_time = models.DateTimeField(blank=True, null=True)
	summary = models.CharField(max_length=200)

	#Defines how an individual instance of this class will return as a string
	def __unicode__(self):
		return self.incident_num

	def __str__(self):
		return self.incident