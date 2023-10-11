from django.views.generic import DetailView
from django_filters.views import FilterView
from spotistats_app.models import SpotifyStats
from spotistats_app.filters.song_filter import SongFilter

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class SongSearchView(FilterView):
    model = SpotifyStats
    filterset_class = SongFilter
    template_name = 'spotistats_app/song_search.html'

    def get_queryset(self):
        # Get the queryset based on the filter settings
        queryset = super().get_queryset()

        # Order the queryset by the "streams" field in descending order
        queryset = queryset.order_by('-streams')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Paginate the queryset
        page = self.request.GET.get('page')
        paginator = Paginator(context['filter'].qs, 15)
        try:
            songs = paginator.page(page)
        except PageNotAnInteger:
            songs = paginator.page(1)
        except EmptyPage:
            songs = paginator.page(paginator.num_pages)

        context['songs'] = songs
        return context


class SongInfoView(DetailView):
    model = SpotifyStats
    template_name = 'spotistats_app/song_info.html'
    context_object_name = 'song'
    pk_url_kwarg = 'song_pk'  # Define the URL keyword for the song's primary key

    def get_queryset(self):
        return SpotifyStats.objects.all()
