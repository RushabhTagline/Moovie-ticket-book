from django.urls import path
from Api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AllMovie.as_view()),
    path('moviedetail/<int:id>',views.MovieDetails.as_view(),name='MovieDetails'),
    path('theatre/<int:id>',views.TheatreDetails.as_view()),
    path('book/<int:show_id>',views.BookSeats.as_view(), name='show-time-list-page'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)