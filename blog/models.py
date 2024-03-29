from django.db import models
from django.utils import timezone

class Post(models.Model):
	autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title

#aaaaaaaaaaaaaa
