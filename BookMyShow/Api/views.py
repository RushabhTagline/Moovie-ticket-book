from rest_framework.response import Response
from rest_framework import status, views
from django.shortcuts import get_object_or_404, render, redirect
from .models import BookSeat, Movie, Theatre, MovieShow
from .serializers import MovieSerializer,ShowSerializer,BookSeatSerializer
from .forms import BookSeatForm
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.


class AllMovie(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request,  *args, **kwargs):
        items = Movie.objects.all() 
        serializer = MovieSerializer(items, many=True)
        return Response({'data': serializer.data})
    
class MovieDetails(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'moviedetails.html'

    def get(self, request, id):
        items = get_object_or_404(Movie, id=id) 
        serializer = MovieSerializer(items)
        return Response({'data': serializer.data})

class TheatreDetails(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'theatrelist.html'

    def get(self, request, id, *args, **kwargs):
        items = MovieShow.objects.filter(movie_name = id).all()
        serializer = ShowSerializer(items, many = True)
        return Response({'items': serializer.data})

class BookSeats(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'seatpage.html'

    def get(self, request, show_id, *args, **kwardgs):
        print(show_id,'\n=-===--=-=--=Get====---=-----===-')
        data = get_object_or_404(BookSeat, show_id=show_id)
        serializer = BookSeatSerializer(data)
        return Response({'serializer':serializer,'data':data})

    def post(self, request, show_id, *args, **kwarg):
        print(show_id,"\n==-=-=-=-===-=-Post==-=-==-===-=--=-=")
        get_data = get_object_or_404(BookSeat, show_id=show_id)
        serializer = BookSeatSerializer(get_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/')
        else:
            return Response({'serializer':serializer,'data':get_data})
        
        