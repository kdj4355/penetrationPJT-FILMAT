from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    released_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_moives', blank=True)


class Actor(models.Model):
    movie = models.ManyToManyField(Movie, related_name='movie_actor')
    name = models.CharField(max_length=50)
    gender = models.IntegerField()
    popularity = models.FloatField()
    profile_path = models.CharField(max_length=200)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actors', blank=True)

