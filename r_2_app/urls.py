from django.urls import path

from . import views

# index is unsed for anything
# songs path all use index template as reference
urlpatterns = \
    [
        path('',views.index , name = 'index'),
        path('songs/',views.list_songs, name = 'list_songs'),
        path('songs/<int:song_id>/',views.list_song, name = 'details'),
        path('songs/<int:song_id>/details/',views.list_songDetails, name = 'moreDetails'),
    ]