from django.contrib import admin
from .models import Movie, Theatre, Show
#Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_type','language','run_length'] 

@admin.register(Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ['id','name','no_of_screen'] 

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ['id','movie_name','theatre','screen','date','start_time'] 