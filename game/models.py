from django.db import models


class Topic(models.Model):
    topic = models.CharField(max_length=30)

    def __str__(self):
        return self.topic


class Word(models.Model):
    picture_url = models.CharField(max_length=250)
    text = models.CharField(max_length=30)
    topic = models.ForeignKey(Topic, related_name='words', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def show_topic(self):
        return self.topic


class Game(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField()
    rope_lenght = models.IntegerField()
    words = models.ManyToManyField(Word)
    guessed_words = models.ManyToManyField(Word, related_name="+")

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if self.is_active and self.guessed_words.count():
    #         for word in self.guessed_words.all():
    #             self.guessed_words.remove(word.id)
    #     super(Game, self).save(*args, **kwargs)

    def number_of_pictures(self):
        return self.words.count()
