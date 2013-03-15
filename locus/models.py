# -*- coding: utf-8 -*-
"""Simple profile app to extend django auth.user using django-userena"""

from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField
from .abstract import SimpleAddressModel

# TODO: allow this to be configurable
# Allows you to use a profile with GIS based location profile or simple
# location_model = getattr(settings, 'PERSONA_LOCATION_MODEL', 'SimpleAddressModel')
# LOCATION_CLASS = getattr(location, location_model)

class Locus(SimpleAddressModel):
    """A location model that can be used to store all location information"""
    pass



