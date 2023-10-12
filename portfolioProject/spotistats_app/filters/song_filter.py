import django_filters
from spotistats_app.models import SpotifyStats
from django import forms

class SongFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        label="Title",
        lookup_expr='istartswith',
        widget=forms.TextInput(
        attrs={ "class":"form-control",
               "placeholder": "Enter song title..."
               }
        )
    )

    released_date = django_filters.DateFilter(
        label="Release Date",
        lookup_expr="gte",
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'data-provide': 'datepicker',  # Add Bootstrap datepicker data attribute
            }
        ),
    )

    OPTIONS = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    danceability_percentage = django_filters.ChoiceFilter(
        label="Danceability",
        choices=OPTIONS,
        lookup_expr='exact',  # Use 'exact' to match the selected choice exactly
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    energy_percentage = django_filters.ChoiceFilter(
        label="Energy Level",
        choices=OPTIONS,
        lookup_expr='exact',  # Use 'exact' to match the selected choice exactly
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    acousticness_percentage = django_filters.ChoiceFilter(
        label="Acoustic Sound",
        choices=OPTIONS,
        lookup_expr='exact',  # Use 'exact' to match the selected choice exactly
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    speechiness_percentage = django_filters.ChoiceFilter(
        label="Spoken Words",
        choices=OPTIONS,
        lookup_expr='exact',  # Use 'exact' to match the selected choice exactly
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = SpotifyStats
        fields = ['title', 'released_date', 'danceability_percentage', 'energy_percentage', 'acousticness_percentage', 'speechiness_percentage']
        order_by = ['']