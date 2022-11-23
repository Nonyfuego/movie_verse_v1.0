from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    casts = models.ManyToManyField('Actor')
    director = models.ForeignKey('Director',on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to='cover_photos/')
    storyline = models.TextField(help_text='Short description about the movie')
    released_year = models.IntegerField()
    released_date = models.DateField()
    genres = models.ManyToManyField('Genre')
    runtime_hour = models.IntegerField()
    runtime_mins = models.IntegerField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='actor_photos')
    birthdate = models.DateField()
    bio = models.TextField(help_text='Enter Actor bio')

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return full_name


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='director_photos/')
    birthdate = models.DateField()
    bio = models.TextField(help_text='Enter Actor bio')

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name + " " + self.last_name


class Genre(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
