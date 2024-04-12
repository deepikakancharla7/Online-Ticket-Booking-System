# movie_api/models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    duration = models.IntegerField()  # Duration in minutes
    synopsis = models.TextField()

class Theater(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    available_seats = models.IntegerField()
