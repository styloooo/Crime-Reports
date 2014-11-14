from django.db import models

# Create your models here.
class Crime(models.Model):
	incident_num = models.CharField(max_length=10, primary_key=True)
	incident = models.CharField(max_length=20, blank=True, null=True)
	attempt = models.BooleanField(blank=True, null=True)
	location = models.CharField(max_length=80)
	#proper_location
	officer = models.CharField(max_length=30)
	date_time = models.DateTimeField(blank=True, null=True)
	summary = models.CharField(max_length=200)