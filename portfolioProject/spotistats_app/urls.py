from django.urls import path
from spotistats_app.views.artist import ArtistSearchView, ArtistInfoView
from spotistats_app.views.song import SongSearchView, SongInfoView

urlpatterns = [
    path('song-search/', SongSearchView.as_view(), name='song-search'),
    path('artist-search/', ArtistSearchView.as_view(), name='artist-search'),
    path('artist-info/<str:artist_name>/', ArtistInfoView.as_view(), name='artist-info'),
    path('song-info/<int:song_pk>/', SongInfoView.as_view(), name='song-info'),
]