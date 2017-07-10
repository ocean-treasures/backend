from django.db import models

class Picture(models.Model):
	pictureUrl = models.CharField(max_length = 250)

	word = models.CharField(max_length = 30)

	def __str__(self):
		return self.word

	def hi(self):
		return "hilll"

	def get_pic(self):
		return self.pictureUrl


class Progress(models.Model):
	curr = models.IntegerField()
	max_progress  = models.IntegerField()
	#rope_lenght = models.IntegerField()