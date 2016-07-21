from django.db import models

class Links(models.Model):
	shorter = models.SlugField(primary_key=True, max_length=4)
	#length > 2000 will not work in most browsers anyway
	original = models.URLField(max_length=2000)
	date_created = models.DateTimeField(auto_now=True)

def __str__(self):
	return self.original