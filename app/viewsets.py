from rest_framework import viewsets

from . import (
    serializers,
    models
)


class ArtistViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.ArtistSerializer
    queryset = models.Artist.objects.all()

class MusicViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.MusicSerializer
    queryset = models.Music.objects.all()

