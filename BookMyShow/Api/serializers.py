from rest_framework import serializers 
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name','movie_type','director','language','run_length','trailer','image']
