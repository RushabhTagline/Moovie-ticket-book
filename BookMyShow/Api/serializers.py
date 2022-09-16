from dataclasses import fields
from rest_framework import serializers
from .models import BookSeat, Movie, MovieShow, Theatre, Screen

    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'movie_type', 'about_us', 'director', 'language', 'run_length', 'trailer', 'image']

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = ['id', 'name', 'address']

class ScreenSrializers(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = ['id', 'theatre_name', 'screen_no']

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShow
        fields = ['id', 'movie_name', 'theatre_name', 'screen_no', 'tecket_price', 'date', 'start_time']

class BookSeatSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BookSeat
        fields = ['id', 'show_id', 'timestamp', 'seat', 'total_amount']

