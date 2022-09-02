from django.contrib import admin
from .models import Movie, Theatre, MovieShow, Screen, BookSeat
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_type','language','run_length'] 

@admin.register(Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ['id','name','address'] 

# @admin.register(TheatreSeat)
# class SeatAdmin(admin.ModelAdmin):
#     list_display = ['id','theatre_name','screen_no']

@admin.register(MovieShow)
class MovieShowAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie_name', 'theatre_name', 'screen_no']

@admin.register(Screen)
class  ScreenAdmin(admin.ModelAdmin):
    list_display = ['id', 'theatre_name', 'screen_no']


@admin.register(BookSeat)
class BookSeatAdmin(admin.ModelAdmin):
    list_display = ['id','show_id','timestamp']