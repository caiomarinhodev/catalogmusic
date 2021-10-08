from app.models import (
    Artist, Music
)
from django.core.exceptions import FieldDoesNotExist


class ArtistMixin(object):

    def kwargs_for_reverse_url(self):
        kwargs_dict = dict()
        if self.model:
            self.object = self.object if self.object is not None else self.get_object()
            try:
                self.model._meta.get_field('slug')
                kwargs_dict['slug'] = self.object.slug
            except FieldDoesNotExist:
                kwargs_dict['pk'] = self.object.id
        return kwargs_dict

    def get_context_data(self, **kwargs):
        context = super(ArtistMixin, self).get_context_data(**kwargs)
        if self.model:
            context['model_name'] = self.model._meta.verbose_name.title()
            context[
                'model_name_plural'] = self.model._meta.verbose_name_plural.title()
        return context

    def get_artist(self):
        return Artist.objects.get(pk=self.kwargs.get("pk_artist", 0))


class MusicMixin(object):

    def kwargs_for_reverse_url(self):
        kwargs_dict = dict()
        if self.model:
            self.object = self.object if self.object is not None else self.get_object()
            try:
                self.model._meta.get_field('slug')
                kwargs_dict['slug'] = self.object.slug
            except FieldDoesNotExist:
                kwargs_dict['pk'] = self.object.id
        return kwargs_dict

    def get_context_data(self, **kwargs):
        context = super(MusicMixin, self).get_context_data(**kwargs)
        if self.model:
            context['model_name'] = self.model._meta.verbose_name.title()
            context[
                'model_name_plural'] = self.model._meta.verbose_name_plural.title()
        return context

    def get_music(self):
        return Music.objects.get(pk=self.kwargs.get("pk_music", 0))
