from django.db import models
from datetime import datetime

# Create your models here.
class sms(models.Model):
	name = models.CharField(max_length=50)
	mobile = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return format(self.name)
