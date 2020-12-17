from django.db import models
# Create your models here.
from django.shortcuts import render
class Music(models.Model):
    song = models.CharField(max_length=256)
    singer = models.CharField(max_length=256)
    mp3 = models.CharField(max_length=256)
    lrc=models.TextField()
class Search(models.Model):
    song = models.CharField(max_length=256)
    singer = models.CharField(max_length=256)
    mp3 = models.CharField(max_length=256)
    lrc=models.TextField()
class Music1(models.Model):
    song = models.CharField(max_length=256)
    singer = models.CharField(max_length=256)
    mp3 = models.CharField(max_length=256)
    lrc=models.TextField()
class Mp3(models.Model):
    song = models.CharField(max_length=256)
    singer = models.CharField(max_length=256)
    mp3 = models.CharField(max_length=256)
    lrc=models.TextField()
    hp = models.CharField(max_length=256,default=None)
    rank=models.CharField(max_length=256,default=None)
class AddList(models.Model):
    song = models.CharField(max_length=256)
    singer = models.CharField(max_length=256)
    mp3 = models.CharField(max_length=256)
    lrc=models.TextField()
    hp = models.CharField(max_length=256,default=None)
    rank=models.CharField(max_length=256,default=None)

