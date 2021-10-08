#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from django.contrib import messages
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.core.exceptions import FieldDoesNotExist
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, DeleteView, UpdateView
)
from django.views.generic.list import ListView

from app.constants import URL_CHORDIFY

try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy, reverse

from app.models import Music
from app.forms import MusicForm
from app.mixins import MusicMixin
from app.conf import MUSIC_DETAIL_URL_NAME, MUSIC_CREATE_URL_NAME, \
    MUSIC_LIST_URL_NAME, MUSIC_UPDATE_URL_NAME, \
    MUSIC_DELETE_URL_NAME


class MusicUpdateMixin(object):
    def get_youtube_id(self, form):
        data = form.cleaned_data
        youtube_url = str(data['youtube_url'])
        youtube_id_start_index = youtube_url.index('?v=')
        youtube_id_finish_index = youtube_url.index('&')
        youtube_id = youtube_url[int(youtube_id_start_index) + 3:int(
            youtube_id_finish_index)]
        return youtube_id

    def get_chords(self, form):
        youtube_id = self.get_youtube_id(form)
        url_chordify = URL_CHORDIFY.format(youtube_id)
        req = requests.get(url_chordify)
        if req.status_code == 200:
            response_chordify = req.json()
            response_chordify['youtube_id'] = youtube_id
            return response_chordify
        return None

    def form_valid(self, form):
        data = form.cleaned_data
        self.object = form.save()
        response_chordify = self.get_chords(form=form)
        self.object.chords = response_chordify['chords']
        self.object.original_tone = response_chordify['derivedKey']
        if data['band_tone']:
            self.object.band_tone = data['band_tone']
        else:
            self.object.band_tone = response_chordify['derivedKey']
        self.object.bpm = response_chordify['derivedBpm']
        self.object.bar_length = response_chordify['barLength']
        self.object.youtube_id = response_chordify['youtube_id']
        messages.success(self.request, 'Music criado com sucesso')
        return super(MusicUpdateMixin, self).form_valid(form)


class List(LoginRequiredMixin, MusicMixin, ListView):
    """
    List all Musics
    """
    login_url = '/admin/login/'
    queryset = Music.objects.all()
    template_name = 'music/list.html'
    model = Music
    context_object_name = 'musics'
    ordering = '-created_at'

    def get_queryset(self):
        return Music.objects.all()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['detail_url_name'] = MUSIC_DETAIL_URL_NAME
        context['delete_url_name'] = MUSIC_DELETE_URL_NAME
        if self.request.user.has_perm("app.add_music"):
            context['create_object_reversed_url'] = reverse_lazy(
                MUSIC_CREATE_URL_NAME
            )

        return context


class Create(LoginRequiredMixin, MusicMixin, MusicUpdateMixin,
             PermissionRequiredMixin,
             CreateView):
    """
    Create a Music
    """
    login_url = '/admin/login/'
    model = Music
    permission_required = (
        'app.add_music'
    )
    form_class = MusicForm
    template_name = 'music/create.html'
    context_object_name = 'music'

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(MUSIC_LIST_URL_NAME)
        return context

    def get_success_url(self):
        return reverse_lazy(MUSIC_DETAIL_URL_NAME,
                            kwargs=self.kwargs_for_reverse_url())

    def get_initial(self):
        data = super(Create, self).get_initial()
        return data

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Create, self).form_invalid(form)


class Detail(LoginRequiredMixin, MusicMixin, DetailView):
    """
    Detail of a Music
    """
    login_url = '/admin/login/'
    model = Music
    template_name = 'music/detail.html'
    context_object_name = 'music'

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(MUSIC_LIST_URL_NAME)
        if self.request.user.has_perm("app.change_music"):
            context['update_object_reversed_url'] = reverse_lazy(
                MUSIC_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("app.delete_music"):
            context['delete_object_reversed_url'] = reverse_lazy(
                MUSIC_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )
        return context


class Update(LoginRequiredMixin, MusicMixin, MusicUpdateMixin,
             PermissionRequiredMixin,
             UpdateView):
    """
    Update a Music
    """
    login_url = '/admin/login/'
    model = Music
    template_name = 'music/update.html'
    context_object_name = 'music'
    form_class = MusicForm
    permission_required = (
        'app.change_music'
    )

    def get_initial(self):
        data = super(Update, self).get_initial()
        return data

    def get_success_url(self):
        return reverse_lazy(MUSIC_DETAIL_URL_NAME,
                            kwargs=self.kwargs_for_reverse_url())

    def get_context_data(self, **kwargs):
        data = super(Update, self).get_context_data(**kwargs)
        data['list_reversed_url'] = reverse_lazy(MUSIC_LIST_URL_NAME)
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Music atualizado com sucesso')
        return super(Update, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Update, self).form_invalid(form)


class Delete(LoginRequiredMixin, MusicMixin, PermissionRequiredMixin,
             DeleteView):
    """
    Delete a Music
    """
    login_url = '/admin/login/'
    model = Music
    permission_required = (
        'app.delete_music'
    )
    template_name = 'music/delete.html'
    context_object_name = 'music'

    def get_context_data(self, **kwargs):
        context = super(Delete, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(MUSIC_LIST_URL_NAME)
        collector = NestedObjects(using='default')
        collector.collect([self.get_object()])
        context['deleted_objects'] = collector.nested()
        return context

    def __init__(self):
        super(Delete, self).__init__()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Music removido com sucesso')
        return super(Delete, self).delete(self.request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(MUSIC_LIST_URL_NAME)
