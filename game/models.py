from django.db import models
from django.utils.html import format_html

class Picture(models.Model):
	pictureUrl = models.CharField(max_length = 250)
	word = models.CharField(max_length = 30)

	def __str__(self):
		return self.word


class Progress(models.Model):
	#curr = models.IntegerField(help_text="Current place of the rope")
	pictures = models.ManyToManyField(Picture)
	max_progress  = models.IntegerField(help_text="Number of pictures for one game")
	rope_lenght = models.IntegerField()

	def __str__(self):
		return 'Game ' + str(self.id)

class Game(models.Model):
	name = models.CharField(max_length = 30)
	rope_lenght = models.IntegerField()
	pictures = models.ManyToManyField(Picture)