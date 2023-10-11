# myapp/management/commands/init_spotify_stats.py

import csv
from django.core.management.base import BaseCommand
from spotifyapp.models import SpotifyStats, Artist
from datetime import datetime

class Command(BaseCommand):
    help = 'Initialize SpotifyStats data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='Path to the CSV file')

    def assign_percentage_label(self, value):
        if value <= 33:
            return 1
        elif value <= 66:
            return 2
        else:
            return 3
        
    def create_datetime(self, year, month, day):
        return datetime(int(year), int(month), int(day))


    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Clear existing data if needed
        #SpotifyStats.objects.all().delete()
        Artist.objects.all().delete()

        with open(csv_file, 'r', encoding='ISO-8859-1') as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                # Create or retrieve Artist objects
                artist_names = [name.strip() for name in row['artist(s)_name'].split(',')]
                artists = [Artist.objects.get_or_create(name=name)[0] for name in artist_names if name != ""]

                # Create the SpotifyStats record with associated artists and assigned labels
                spotify_stats = SpotifyStats.objects.create(
                    title=row['track_name'],
                    released_date=self.create_datetime(row['released_year'], row['released_month'], row['released_day']),
                    in_spotify_playlists=row['in_spotify_playlists'],
                    in_spotify_charts=row['in_spotify_charts'],
                    streams=row['streams'],
                    bpm=row['bpm'],
                    danceability_percentage=self.assign_percentage_label(int(row['danceability_percentage'])),
                    energy_percentage=self.assign_percentage_label(int(row['energy_percentage'])),
                    acousticness_percentage=self.assign_percentage_label(int(row['acousticness_percentage'])),
                    speechiness_percentage=self.assign_percentage_label(int(row['speechiness_percentage']))
                )
                # Connects the artist to the stat record
                spotify_stats.artists.set(artists)
                self.stdout.write(self.style.SUCCESS(f'Successfully initialized {row["track_name"]}'))
                

            self.stdout.write(self.style.SUCCESS('Successfully initialized data from CSV'))
