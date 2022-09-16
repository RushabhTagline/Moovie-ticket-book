from faulthandler import disable
from tkinter import DISABLED
from django.utils import timezone
from multiselectfield import MultiSelectField
import string
from django.db import models

# Create your models here.

class Movie(models.Model):
    lang_choice = (
        ('', 'Select language'),
        ('ENGLISH', 'English'),
        ('Gujarati', 'Gujarati'),
        ('BENGALI', 'Bengali'),
        ('HINDI', 'Hindi'),
        ('TAMIL', 'Tamil'),
        ('TELUGU', 'Telugu'),
    )
    type_choice = (
        ('', 'Select movie type'),
        ('Action', 'Action'),   
        ('Comedy', 'Comedy'),
        ('Crime & Gangster', 'Crime & Gangster'),
        ('Drama', 'Drama'),
    )
    name = models.CharField(max_length=20,blank=False)
    movie_type = models.CharField(max_length=100,choices=type_choice,blank=False)
    about_us = models.CharField(max_length=255)
    director = models.CharField(max_length=20,null=True,blank=True)
    language = models.CharField(max_length=10, choices=lang_choice)
    run_length = models.IntegerField(help_text="Etern run length in minutes",blank=False)
    trailer = models.URLField(blank=True)
    image = models.ImageField()

    def __str__(self):
        return str(self.id) + ' : ' + self.name

    class Meta:
        ordering = ['id']

class Theatre(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return str(self.id) + ' : ' + self.name

class Screen(models.Model):
    theatre_name = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen_no = models.IntegerField(default=1,unique=True)

    def __str__(self):
        return str(self.screen_no)

class MovieShow(models.Model):
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre_name = models.ForeignKey(Theatre, on_delete=models.CASCADE,)
    screen_no = models.ForeignKey(Screen,on_delete=models.CASCADE)
    tecket_price = models.IntegerField(default=220)
    date = models.DateField()
    start_time = models.TimeField()

    def __str__(self):
        return str(self.id) + ' ( ' + str(self.movie_name) + ' ) '

def seats():
    seatDict = {}
    seat_rows = 10
    seat_cols = 16
    # print(string.ascii_uppercase[:seat_rows])
    for row in string.ascii_uppercase[:seat_rows]:
        for seatNumber in range(1, seat_cols+1):
            seatDict[row +str(seatNumber)]=row +str(seatNumber)
    seatList = list(seatDict.items())
    return seatList
        
class BookSeat(models.Model):
    show_id = models.ForeignKey(MovieShow,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    seat = MultiSelectField(choices=seats(), unique = True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ('seat', 'show_id')