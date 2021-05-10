from rest_framework import serializers, viewsets, status
from .models import Artist
from .serializers import ArtistSerializer, ArtistSaveSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect

@csrf_protect
class ArtistViewSet(viewsets.ModelViewSet):
    @api_view(['GET', 'POST'])
    def artist_list(self, format=None):
        if self.method == 'GET':
            artists = Artist.objects.all()
            artist_serializer = ArtistSerializer(artists, many=True)
            return Response(artist_serializer.data, status=status.HTTP_200_OK)
        elif self.method == 'POST':
            artist_serializer = ArtistSaveSerializer(data=self.data)
            if artist_serializer.is_valid():
                artist_serializer.save()
                return Response(artist_serializer.data, status=status.HTTP_201_CREATED)
            return Response(artist_serializer.error, status=status.HTTP_400_BAD_REQUEST)

    
    @api_view(['PUT', 'DELETE', 'GET'])
    def artist_detail(self, artistId):
        artist = Artist.objects.get(pk=artistId)
        if self.method == 'PUT':
            artist_serializer = ArtistSaveSerializer(artist, data=self.data)
            if artist_serializer.is_valid():
                artist_serializer.save()
                return Response(artist_serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(artist_serializer.error, status=status.HTTP_400_BAD_REQUEST)
        elif self.method == 'DELETE':
            artist.delete()
            return Response({'message':'Artist was deleted successfully'}, status=status.HTTP_202_ACCEPTED)
        elif self.method == 'GET':
            artist_serializer = ArtistSerializer(artist)
            return Response(artist_serializer.data, status=status.HTTP_200_OK)
            