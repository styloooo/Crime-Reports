from django.db import models

# Create your models here.
class Agency(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	address = models.CharField(max_length=100, null=True)
	latitude = models.FloatField(max_length=100, null=True)
	longitude = models.FloatField(max_length=100, null=True)
	agency = models.ForeignKey(Agency)
	intersection = models.BooleanField(default=False)
	block = models.BooleanField(default=False)
	city = models.CharField(max_length=70, null=True, blank=True)

	def __unicode__(self):
		return self.address

class Officer(models.Model):
	name = models.CharField(max_length=50)
	badge_num = models.IntegerField(null=True)
	agency = models.ForeignKey(Agency)

	def __unicode__(self):
		return self.name

class Crime(models.Model):
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=255, null=True)
	arrests = models.IntegerField(default=0)
	total_count = models.IntegerField(default=0)
	description = models.TextField(max_length=255, null=True, blank=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Crime, self).save(*args, **kwargs)

class Race(models.Model):
	name = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name

class Offender(models.Model):
	name = models.CharField(max_length=50)
	race = models.ForeignKey(Race)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

class Victim(models.Model):
	age = models.IntegerField(default = 0)
	sex = models.CharField(max_length=1, null=True)
	name = models.CharField(max_length=50, null=True)
	origin = models.CharField(max_length=50, null=True)

	def __unicode__(self):
		return self.age

class Arrestee(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(default = 0)
	sex = models.CharField(max_length=1, null=True)
	address = models.ForeignKey(Location)
	race = models.ForeignKey(Race)

	def __unicode__(self):
		return self.name

class Arrest(models.Model):
	arrestee = models.ForeignKey(Arrestee)
	charges = models.ForeignKey(Crime)
	location = models.ForeignKey(Location)
	officer = models.ForeignKey(Officer)
	datetime = models.DateTimeField()

	def __unicode__(self):
		return self.arrestee.name

class Property(models.Model):
	loss = models.CharField(max_length=15)
	thing = models.CharField(max_length=50)

	def __unicode__(self):
		return self.thing

class Incident(models.Model):
	agency = models.ForeignKey(Agency)
	code = models.CharField(max_length=20)
	datetime_occurred = models.DateTimeField(null = True)
	datetime_reported = models.DateTimeField(null = True)
	summary = models.TextField()

	officer = models.ForeignKey(Officer)
	location_occurred = models.ForeignKey(Location)

	crimes = models.ManyToManyField(Crime)
	arrests = models.ManyToManyField(Arrest, null=True)
	offenders = models.ManyToManyField(Offender, null=True)
	properties = models.ManyToManyField(Property, null=True)

	raw_entry = models.TextField(null=True)

	def __unicode__(self):
		return self.code

	def save(self, *args, **kwargs):
		super(Incident, self).save(*args, **kwargs)
