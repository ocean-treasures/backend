import sys

from constance import config
from django.db import models
sys.path.insert(0, r'/home/pi/ocean_motion')
from motion import move


class Topic(models.Model):
    topic = models.CharField(max_length=30)

    def __str__(self):
        return self.topic


class Picture(models.Model):
    pictureUrl = models.CharField(max_length=250)
    word = models.CharField(max_length=30)
    topic = models.ForeignKey(Topic, related_name='picture', null=True)

    def __str__(self):
        return self.word

    def show_topic(self):
        return self.topic


class Game(models.Model):
    name = models.CharField(max_length=30)
    active = models.BooleanField()
    pictures = models.ManyToManyField(Picture, related_name='game')
    current = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        active_game = Game.objects.get(active=True)
        for i in range(0, active_game.current):
            motor_move = motor_move = config.ROPE_LENGHT / active_game.number_of_pictures()
            move((motor_move * config.GOING_UP), clockwise=True, async=False)
        if self.active:
            Game.objects.filter(active=True).update(current=0)
            Game.objects.filter(active=True).update(active=False)
            self.active = True
        super(Game, self).save(*args, **kwargs)

    def number_of_pictures(self):
        return self.pictures.count()
