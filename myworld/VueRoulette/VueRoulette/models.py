from django.db import models


class record(models.Model):
  highscore = models.IntegerField()
  playername = models.CharField(max_length=100)