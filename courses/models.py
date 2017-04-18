from __future__ import unicode_literals

from django.db import models

# model for a course.
class Course(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	description = models.TextField()

	# If a type string is called on this object, it will return the title
	def __str__(self):
		return self.title


# model for a step in a course
class Step(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	order = models.IntegerField(default = 0)
	course = models.ForeignKey(Course)

	def __str__(self):
		return self.title