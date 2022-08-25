from django.db import models
from django.conf import settings
# Create your models here.


class Movie(models.Model):
    lang_choice = (
        ('', 'Select language'),
        ('ENGLISH', 'English'),
        ('BENGALI', 'Bengali'),
        ('HINDI', 'Hindi'),
        ('TAMIL', 'Tamil'),
        ('TELUGU', 'Telugu'),
    )
    type_choice = (
        ('', 'Select movie type'),
        ('Action Films', 'Action Films'),
        ('Comedy Films', 'Comedy Films'),
        ('Crime & Gangster Films', 'Crime & Gangster Films'),
        ('Drama Films', 'Drama Films'),
    )
    name = models.CharField(max_length=20,null=False,blank=False)
    movie_type = models.CharField(max_length=100,choices=type_choice,null=False,blank=False)
    director = models.CharField(max_length=20,null=True,blank=True)
    language = models.CharField(max_length=10, choices=lang_choice)
    run_length = models.IntegerField(help_text="Enter run length in minutes",null=False,blank=False)
    trailer = models.URLField(blank=True)
    image = models.ImageField()

    def __str__(self):  
        return self.name


class Theatre(models.Model):
    name = models.CharField(max_length=50,null=False)
    address = models.CharField(max_length=100)
    no_of_screen = models.IntegerField()

    def __str__(self):
        return self.name 

class Show(models.Model):
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE,null=False)
    screen = models.IntegerField(default=1)
    date = models.DateField()
    start_time = models.TimeField()