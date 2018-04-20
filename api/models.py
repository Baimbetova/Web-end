from django.db import models
from datetime import datetime

# Create your models here.
class BlogApi(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_at = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.title
# Create your models here.
