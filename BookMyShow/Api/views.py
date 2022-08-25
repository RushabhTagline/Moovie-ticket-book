from django.shortcuts import get_object_or_404
from rest_framework import generics, status,views
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Movie,Theatre, Show
from .serializers import MovieSerializer
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
        items = Show.objects.filter(movie_name = item).all()
        time_list = []
        for i in items:
            time_list.append(i.start_time)
        print(time_list,"\n=-=-=-=-=-=-=-==-=-=-=---")
        return Response({'data': items})