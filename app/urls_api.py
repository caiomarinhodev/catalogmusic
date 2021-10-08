from rest_framework.routers import DefaultRouter
from app import (
    viewsets
)

api_urlpatterns = []

artist_router = DefaultRouter()

artist_router.register(
    r'^api/artist',
    viewsets.ArtistViewSet,
    basename="artist"
)

api_urlpatterns += artist_router.urls
music_router = DefaultRouter()

music_router.register(
    r'^api/music',
    viewsets.MusicViewSet,
    basename="music"
)

api_urlpatterns += music_router.urls
