from django.db import models

class Pictures(models.Model):
	pictureUrl = models.CharField(max_length = 250)
	pic_id = models.IntegerField(primary_key = True)
	word = models.CharField(max_length = 30)

class Progress(models.Model):
	curr = models.IntegerField()
	max_progress  = models.IntegerField() 