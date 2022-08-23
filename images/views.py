import os
from django.shortcuts import render
from .models import Image
from .serializers.serializers import ImageSerializer
from rest_flex_fields.views import FlexFieldsModelViewSet
from rest_framework.views import APIView
from test1.tasks import task1, task2, task3, task4
from rest_framework.response import Response
from rest_framework import status
from test1.settings import MEDIA_ROOT


class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ImageWork(APIView):

    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        step = None
        file_exists = os.path.exists(MEDIA_ROOT + '/images/{}'.format(request.POST['image_name']))
        if file_exists is True:
            if 'step' in request.POST:
                pass
                return Response({'': 'ok'}, status=status.HTTP_201_CREATED)
            else:
                pass
        else:
            return Response({'Error': 'No se pudo encontrar el archivo.'}, status=status.HTTP_404_NOT_FOUND)

