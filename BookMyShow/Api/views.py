from re import template
from turtle import Screen
import string
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status,views
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import BookSeat, Movie, Theatre, MovieShow
# Create your views here.


class AllMovie(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    def get(self, request):
        if 'item_id' in request.session:
            del request.session['item_id']
        items = Movie.objects.all() 
        return Response({ 'data': items})
    
class MovieDetails(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'moviedetails.html'

    def get(self, request, id):
        items = get_object_or_404(Movie, id=id) 
        item_id = items.id
        request.session['item_id'] = item_id
        return Response({'data': items})

class TheatreDetails(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'theatrelist.html'

    def get(self, request):
        item = request.session['item_id']
        items = MovieShow.objects.filter(movie_name = item).all()
        return Response({'data': items})

# class SeatArrangement(views.APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'seatpage.html'
