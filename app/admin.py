#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from app.models import *


# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    list_filter = []
    inlines = []
    list_display = ['name', 'id',]


admin.site.register(Artist, ArtistAdmin)


class MusicAdmin(admin.ModelAdmin):
    list_filter = []
    inlines = []
    list_display = ['id', 'title', 'artist']


admin.site.register(Music, MusicAdmin)
