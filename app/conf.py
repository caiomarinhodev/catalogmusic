#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
Global variables for base module
"""
from django.utils.translation import ugettext_lazy as _
from django.conf import LazySettings

settings = LazySettings()


def get_from_settings_or_default(var_name, default):
    try:
        return settings.__getattr__(var_name)
    except AttributeError:
        return default


# Items by page on paginator views
ITEMS_BY_PAGE = 10

CREATE_SUFFIX = "_create"
LIST_SUFFIX = "_list"
DETAIL_SUFFIX = "_detail"
UPDATE_SUFFIX = "_update"
DELETE_SUFFIX = "_delete"

API_SUFFIX = "_api"
style = "base_django/flexbox"


# Messages
OBJECT_CREATED_SUCCESSFULLY = _("Object created successfully")
OBJECT_UPDATED_SUCCESSFULLY = _("Object updated successfully")
OBJECT_DELETED_SUCCESSFULLY = _("Object deleted successfully")

BASE_MODELS_TRANSLATION_NAME = _("Name")
BASE_MODELS_TRANSLATION_DESCRIPTION = _("Description")
BASE_MODELS_TRANSLATION_SLUG = _("Slug")
BASE_MODELS_TRANSLATION_CREATED = _("Created")
BASE_MODELS_TRANSLATION_MODIFIED = _("Modified")
BASE_MODELS_TRANSLATION_ACTIVE = _("Active")

CONFIGURING_APPLICATION = _("Configuring application {}")
CREATING_PERMISSION_WITH_NAME = _("Creating Permission with name {}")
CREATING_GROUP_WITH_NAME = _("Creating Group with name {}")


ARTIST_PREFIX = "ARTIST"

ARTIST_VERBOSE_NAME = _("Artist")
ARTIST_VERBOSE_NAME_PLURAL = _("Artist")

ARTIST_LIST_URL_NAME = ARTIST_PREFIX + LIST_SUFFIX
ARTIST_CREATE_URL_NAME = ARTIST_PREFIX + CREATE_SUFFIX
ARTIST_DETAIL_URL_NAME = ARTIST_PREFIX + DETAIL_SUFFIX
ARTIST_UPDATE_URL_NAME = ARTIST_PREFIX + UPDATE_SUFFIX
ARTIST_DELETE_URL_NAME = ARTIST_PREFIX + DELETE_SUFFIX


MUSIC_PREFIX = "MUSIC"

MUSIC_VERBOSE_NAME = _("Music")
MUSIC_VERBOSE_NAME_PLURAL = _("Music")

MUSIC_LIST_URL_NAME = MUSIC_PREFIX + LIST_SUFFIX
MUSIC_CREATE_URL_NAME = MUSIC_PREFIX + CREATE_SUFFIX
MUSIC_DETAIL_URL_NAME = MUSIC_PREFIX + DETAIL_SUFFIX
MUSIC_UPDATE_URL_NAME = MUSIC_PREFIX + UPDATE_SUFFIX
MUSIC_DELETE_URL_NAME = MUSIC_PREFIX + DELETE_SUFFIX

