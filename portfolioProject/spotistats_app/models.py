from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    def total_million_streams(self):
        total = 0
        for spotify_stat in self.spotifystats_set.all():
            total += spotify_stat.streams

        return round(total/100000)
    
    def avg_bpm(self):
        total_bpm = 0
        count = 0

        # Iterate through the related SpotifyStats objects
        for spotify_stat in self.spotifystats_set.all():
            total_bpm += spotify_stat.bpm
            count += 1

        # Calculate the average BPM and handle division by zero
        if count > 0:
            average_bpm = total_bpm / count
            return round(average_bpm)
        else:
            return 0 
        
    def in_playlists(self):
        # Initialize a variable to store the total in_spotify_playlists count
        total_playlists = 0

        # Iterate through the related SpotifyStats objects
        for spotify_stat in self.spotifystats_set.all():
            total_playlists += spotify_stat.in_spotify_playlists

        # Return the total count of in_spotify_playlists
        return total_playlists
    
    def low_medium_high_counts(self, field_name):
        # Initialize counters for low, medium, and high
        low_count = 0
        medium_count = 0
        high_count = 0

        # Iterate through the related SpotifyStats objects
        for spotify_stat in self.spotifystats_set.all():
            value = getattr(spotify_stat, field_name)
            if value == 1:
                low_count += 1
            elif value == 2:
                medium_count += 1
            elif value == 3:
                high_count += 1

        return [low_count, medium_count, high_count]

PERCENTAGE_CHOICES = (
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High')
)

class SpotifyStats(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist)
    released_date = models.DateField(default=timezone.now)
    in_spotify_playlists = models.PositiveIntegerField()
    in_spotify_charts = models.PositiveIntegerField()
    streams = models.PositiveIntegerField()
    bpm = models.PositiveIntegerField()
    danceability_percentage = models.PositiveSmallIntegerField(choices=PERCENTAGE_CHOICES)
    energy_percentage = models.PositiveSmallIntegerField(choices=PERCENTAGE_CHOICES)
    acousticness_percentage = models.PositiveSmallIntegerField(choices=PERCENTAGE_CHOICES)
    speechiness_percentage = models.PositiveSmallIntegerField(choices=PERCENTAGE_CHOICES)

    def __str__(self):
        return f"{self.title}, {self.artists} {self.in_spotify_charts}"
