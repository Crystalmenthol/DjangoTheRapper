from rest_framework import serializers, viewsets, status
from .models import Single
from .serializers import SingleSerializer, SingleSaveSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect

@csrf_protect
class SingleViewSet(viewsets.ModelViewSet):
    @api_view(['get'])
    def single_list(self, format=None):
        singles = Single.objects.all()
        single_serializer = SingleSerializer(singles, many=True)
        return Response(single_serializer.data)


    @api_view(['post'])
    def create_single(self, format=None):
        single_serializer = SingleSaveSerializer(data=self.data)
        if single_serializer.is_valid():
            single_serializer.save()
            return Response(single_serializer.data, status=status.HTTP_201_CREATED)
        return Response(single_serializer.error, status=status.HTTP_400_BAD_REQUEST)