from django import forms
from django.forms import ModelForm
from app.utils import generate_bootstrap_widgets_for_all_fields

from . import (
    models
)


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone'
            if field_name == 'numero' or field_name == 'number':
                field.widget.attrs['class'] = 'form-control numero'


class ArtistForm(BaseForm, ModelForm):
    class Meta:
        model = models.Artist
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Artist)

    def __init__(self, *args, **kwargs):
        super(ArtistForm, self).__init__(*args, **kwargs)


class MusicForm(BaseForm, ModelForm):
    class Meta:
        model = models.Music
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Music)

    def __init__(self, *args, **kwargs):
        super(MusicForm, self).__init__(*args, **kwargs)
