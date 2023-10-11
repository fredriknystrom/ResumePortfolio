from spotistats_app.models import Artist
from spotistats_app.models import SpotifyStats
from django.views.generic import ListView
from django_filters.views import FilterView
from spotistats_app.filters.artist_filter import ArtistFilter
from spotistats_app.utils import create_low_medium_high_pie_plot
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ArtistSearchView(FilterView):
    model = Artist
    filterset_class = ArtistFilter
    template_name = 'spotifyapp/artist_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Paginate the queryset
        page = self.request.GET.get('page')
        paginator = Paginator(context['filter'].qs, 15)
        try:
            artists = paginator.page(page)
        except PageNotAnInteger:
            artists = paginator.page(1)
        except EmptyPage:
            artists = paginator.page(paginator.num_pages)

        context['artists'] = artists
        return context



class ArtistInfoView(ListView):
    model = SpotifyStats
    template_name = 'spotifyapp/artist_info.html'
    context_object_name = 'records'

    def get_queryset(self):
        # Get the artist's name from the URL parameter
        artist_name = self.kwargs.get('artist_name')
   
        # Retrieve all SpotifyStats records related to the artist
        return SpotifyStats.objects.filter(artists__name=artist_name).order_by('-streams')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist_name = self.kwargs.get('artist_name')
        context['artist_name'] = artist_name
        artist = Artist.objects.get(name=artist_name)
        context['artist'] = artist
        context['dance'] = create_low_medium_high_pie_plot(artist.low_medium_high_counts('danceability_percentage'))
        context['energy'] = create_low_medium_high_pie_plot(artist.low_medium_high_counts('energy_percentage'))
        context['acoustic'] = create_low_medium_high_pie_plot(artist.low_medium_high_counts('acousticness_percentage'))
        context['speech'] = create_low_medium_high_pie_plot(artist.low_medium_high_counts('speechiness_percentage'))
        return context