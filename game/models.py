from django.db import models
#from django.utils.html import format_html
#from material.frontend import Module

#class Sample(Module):
#    icon = 'mdi-image-compare'


class Picture(models.Model):
	pictureUrl = models.CharField(max_length = 250)
	word = models.CharField(max_length = 30)

	def __str__(self):
		return self.word

class Progress(models.Model):
	#curr =  models.IntegerField()
	pictures = models.ManyToManyField(Picture)
	max_progress  = models.IntegerField(help_text="Number of pictures for one game")
	rope_lenght = models.IntegerField()

	def __str__(self):
		return 'Game ' + str(self.id)

class Game(models.Model):
	name = models.CharField(max_length = 30)
	active = models.BooleanField()
	rope_lenght = models.IntegerField()
	pictures = models.ManyToManyField(Picture, related_name='game')
	current = models.IntegerField(default = 0)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		Game.objects.filter(active = True)
		if self.active == True:
			active = Game.objects.filter(active = True).update(active = False)
			
			self.active = True
		super(Game, self).save(*args, **kwargs)
		#super(Game).save(*args, **kwargs)
		#active_games = Game.objects.filter(active = True)
		#Game.objects.filter(active = True).update(active = False)
		#self.active = True
		#self.save()	

	def number_of_pictures(self):
		return self.pictures.count()