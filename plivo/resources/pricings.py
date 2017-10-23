# -*- coding: utf-8 -*-
"""
Pricing class - along with its list class
"""

from plivo.base import PlivoResource, PlivoResourceInterface
from plivo.utils import to_param_dict
from plivo.utils.validators import *


class Pricing(PlivoResource):
    _name = 'Pricing'
    _identifier_string = 'country_iso'

    def get(self):
        return self.client.pricing.get(self.id)


class Pricings(PlivoResourceInterface):
    _resource_type = Pricing

    @validate_args(country_iso=[regex(r'^[A-Z]{2}$')])
    def get(self, country_iso):
        return self.client.request(
            'GET', ('Pricing', ),
            to_param_dict(self.get, locals()),
            response_type=Pricing)
