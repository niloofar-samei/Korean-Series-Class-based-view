from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=200, unique=True)
    released_year = models.IntegerField(default=0)
    voteup = models.IntegerField(default=0)
    movie_image = models.ImageField(upload_to="movie/", blank=True, null=True)
    movie_about = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.movie_name


class Actor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor_name = models.CharField(max_length=200)
    actor_image = models.ImageField(upload_to="actor/", blank=True, null=True)

    def __str__(self):
        return self.actor_name


class Actress(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actress_name = models.CharField(max_length=200)
    actress_image = models.ImageField(upload_to="actress/", blank=True, null=True)

    def __str__(self):
        return self.actress_name
