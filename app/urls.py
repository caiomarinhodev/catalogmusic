from django.urls import path

from app import conf

from app.urls_api import api_urlpatterns

urlpatterns = []

from app.views import artist
urlpatterns += [

    # artist
    path(
        '',
        artist.List.as_view(),
        name=conf.ARTIST_LIST_URL_NAME
    ),
    path(
        'artist/create/',
        artist.Create.as_view(),
        name=conf.ARTIST_CREATE_URL_NAME
    ),
    path(
        'artist/<int:pk>/',
        artist.Detail.as_view(),
        name=conf.ARTIST_DETAIL_URL_NAME
    ),
    path(
        'artist/<int:pk>/update/',
        artist.Update.as_view(),
        name=conf.ARTIST_UPDATE_URL_NAME
    ),
    path(
        'artist/<int:pk>/delete/',
        artist.Delete.as_view(),
        name=conf.ARTIST_DELETE_URL_NAME
    ),
]

from app.views import music
urlpatterns += [
    # music
    path(
        'music/',
        music.List.as_view(),
        name=conf.MUSIC_LIST_URL_NAME
    ),
    path(
        'music/create/',
        music.Create.as_view(),
        name=conf.MUSIC_CREATE_URL_NAME
    ),
    path(
        'music/<int:pk>/',
        music.Detail.as_view(),
        name=conf.MUSIC_DETAIL_URL_NAME
    ),
    path(
        'music/<int:pk>/update/',
        music.Update.as_view(),
        name=conf.MUSIC_UPDATE_URL_NAME
    ),
    path(
        'music/<int:pk>/delete/',
        music.Delete.as_view(),
        name=conf.MUSIC_DELETE_URL_NAME
    ),
]

urlpatterns += api_urlpatterns
