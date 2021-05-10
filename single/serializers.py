from rest_framework import serializers
from .models import Single

class SingleSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    class Meta:
        model = Single
        fields = '__all__'

    def get_artist(self, instance):
        return instance.artist.aka


class SingleSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Single
        fields = ['name', 'youtube_views', 'artist']