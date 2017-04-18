from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	description = models.TextField()

	# If a type string is called on this object, it will return the title
	def __str__(self):
		return self.title