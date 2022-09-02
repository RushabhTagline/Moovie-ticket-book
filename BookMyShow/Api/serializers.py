from rest_framework import serializers 
from .models import Movie, MovieShow, Theatre
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShow
        fields = '__all__'

