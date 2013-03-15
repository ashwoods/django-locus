# -*- coding: utf-8 -*-
"""Simple location model to use in django apps"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField


class SimpleAddressModel(TimeStampedModel):
    """Base Model for Address models"""
    address = models.CharField(_('Address Line 1'), max_length=100, blank=True)
    address_extra = models.CharField(_('Address Line 2'), max_length=100, blank=True)
    city = models.CharField(_('City'), max_length=50, blank=True)
    state_or_province = models.CharField(_('State or province'), max_length=50, blank=True)
    country = CountryField(_('Country'), blank=True)
    postal_code = models.CharField(_('Postal code'), max_length=10, blank=True)


    def __unicode__(self):
        return self.formatted_address

    @property
    def formatted_address(self):
        return "%s %s %s" % (self.address, self.city, self.postal_code, self.country)

    class Meta:
        abstract = True
