from django.db import models

class Picture(models.Model):
	pictureUrl = models.CharField(max_length = 250)

	word = models.CharField(max_length = 30)

	def __str__(self):
		return self.word


class Progress(models.Model):
	curr = models.IntegerField(help_text="This is the grey text")
	max_progress  = models.IntegerField()
	rope_lenght = models.IntegerField()