from django.db import models
from datetime import datetime

# Create your models here.

class Cookie(models.Model):
	cookie = models.CharField(max_length=100, blank=False)
	timestamp = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.cookie