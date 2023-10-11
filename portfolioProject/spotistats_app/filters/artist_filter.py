import django_filters
from spotistats_app.models import Artist, SpotifyStats
from django import forms

class ArtistFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label="Artist Name",
        lookup_expr='istartswith',
        widget=forms.TextInput(
        attrs={ "class":"form-control",
               "placeholder": "Enter artist here..."}
        )
    )

    class Meta:
        model = Artist
        fields = ['name']