from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'aka', 'name', 'age']


class ArtistSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['aka', 'name', 'age']