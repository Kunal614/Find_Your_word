from django.db import models

# Create your models here.

class Word(models.Model):

    word = models.CharField(max_length=26 , default=None)

class Sentence(models.Model):
    sentence = models.TextField(max_length = 200 , default=None)

