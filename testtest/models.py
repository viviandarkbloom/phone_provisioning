from django.db import models

# Create your models here.

class Phone(models.Model):
	mac = models.CharField(max_length=12)
	ext = models.IntegerField(max_length=5)
	server = models.CharField(max_length=20)
	isnew = models.BooleanField(default=False)
	def __unicode__(self):
		return self.mac

class Ext(models.Model):
	extension = models.ForeignKey(Phone)
	def __unicode__(self):
		return self.ext
