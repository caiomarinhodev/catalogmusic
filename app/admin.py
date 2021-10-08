#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.apps import apps
from django.contrib import admin

# Register your models here.

from app.models import *


def approve_selected(modeladmin, request, queryset):
    queryset.update(is_approved=True)


def desapprove_selected(modeladmin, request, queryset):
    queryset.update(is_approved=False)


approve_selected.short_description = "Aprovar itens selecionados"
desapprove_selected.short_description = "Desaprovar itens selecionados"


class ArtistAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = [field.name for field in Artist._meta.get_fields()]
    actions = [approve_selected, desapprove_selected]

admin.site.register(Artist, ArtistAdmin)


class MusicAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = [field.name for field in Music._meta.get_fields()]
    actions = [approve_selected, desapprove_selected]

admin.site.register(Music, MusicAdmin)
