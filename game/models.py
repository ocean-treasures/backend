from django.db import models


class Topic(models.Model):
    topic = models.CharField(max_length=30)

    def __str__(self):
        return self.topic


class Picture(models.Model):
    pictureUrl = models.CharField(max_length=250)
    word = models.CharField(max_length=30)
    topic = models.ForeignKey(Topic, related_name='picture', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.word

    def show_topic(self):
        return self.topic


class Game(models.Model):
    name = models.CharField(max_length=30)
    active = models.BooleanField()
    rope_lenght = models.IntegerField()
    pictures = models.ManyToManyField(Picture, related_name='game')
    current = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.active:
            Game.objects.filter(active=True).update(current=0, active=False)
            self.active = True
        super(Game, self).save(*args, **kwargs)

    def number_of_pictures(self):
        return self.pictures.count()
