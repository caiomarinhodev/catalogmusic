#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import FieldDoesNotExist
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, DeleteView, UpdateView
)
from django.views.generic.list import ListView


try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy, reverse

from app.models import Artist
from app.forms import ArtistForm
from app.mixins import ArtistMixin
from app.conf import ARTIST_DETAIL_URL_NAME, ARTIST_CREATE_URL_NAME, \
ARTIST_LIST_URL_NAME, ARTIST_UPDATE_URL_NAME, \
ARTIST_DELETE_URL_NAME


class List(LoginRequiredMixin, ArtistMixin, ListView):
    """
    List all Artists
    """
    login_url = '/admin/login/'
    queryset = Artist.objects.all()
    template_name = 'artist/list.html'
    model = Artist
    context_object_name = 'artists'
    ordering = '-created_at'

    def get_queryset(self):
        return Artist.objects.all()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['detail_url_name'] = ARTIST_DETAIL_URL_NAME
        context['delete_url_name'] = ARTIST_DELETE_URL_NAME
        if self.request.user.has_perm("app.add_artist"):
            context['create_object_reversed_url'] = reverse_lazy(
                ARTIST_CREATE_URL_NAME
            )
        
        return context


class Create(LoginRequiredMixin, ArtistMixin, PermissionRequiredMixin, CreateView):
    """
    Create a Artist
    """
    login_url = '/admin/login/'
    model = Artist
    permission_required = (
        'app.add_artist'
    )
    form_class = ArtistForm
    template_name = 'artist/create.html'
    context_object_name = 'artist'

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(ARTIST_LIST_URL_NAME)
        return context

    def get_success_url(self):
        return reverse_lazy(ARTIST_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())

    def get_initial(self):
        data = super(Create, self).get_initial()
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Artist criado com sucesso')
        return super(Create, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Create, self).form_invalid(form)


class Detail(LoginRequiredMixin, ArtistMixin, DetailView):
    """
    Detail of a Artist
    """
    login_url = '/admin/login/'
    model = Artist
    template_name = 'artist/detail.html'
    context_object_name = 'artist'

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(ARTIST_LIST_URL_NAME)
        if self.request.user.has_perm("app.change_artist"):
            context['update_object_reversed_url'] = reverse_lazy(
                ARTIST_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("app.delete_artist"):
            context['delete_object_reversed_url'] = reverse_lazy(
                ARTIST_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )
        return context


class Update(LoginRequiredMixin, ArtistMixin, PermissionRequiredMixin, UpdateView):
    """
    Update a Artist
    """
    login_url = '/admin/login/'
    model = Artist
    template_name = 'artist/update.html'
    context_object_name = 'artist'
    form_class = ArtistForm
    permission_required = (
        'app.change_artist'
    )

    def get_initial(self):
        data = super(Update, self).get_initial()
        return data

    def get_success_url(self):
        return reverse_lazy(ARTIST_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())

    def get_context_data(self, **kwargs):
        data = super(Update, self).get_context_data(**kwargs)
        data['list_reversed_url'] = reverse_lazy(ARTIST_LIST_URL_NAME)
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Artist atualizado com sucesso')
        return super(Update, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Update, self).form_invalid(form)


class Delete(LoginRequiredMixin, ArtistMixin, PermissionRequiredMixin, DeleteView):
    """
    Delete a Artist
    """
    login_url = '/admin/login/'
    model = Artist
    permission_required = (
        'app.delete_artist'
    )
    template_name = 'artist/delete.html'
    context_object_name = 'artist'

    def get_context_data(self, **kwargs):
        context = super(Delete, self).get_context_data(**kwargs)
        context['list_reversed_url'] = reverse_lazy(ARTIST_LIST_URL_NAME)
        collector = NestedObjects(using='default')
        collector.collect([self.get_object()])
        context['deleted_objects'] = collector.nested()
        return context

    def __init__(self):
        super(Delete, self).__init__()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Artist removido com sucesso')
        return super(Delete, self).delete(self.request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(ARTIST_LIST_URL_NAME)
