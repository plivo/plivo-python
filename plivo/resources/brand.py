# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import ListResponseObject, PlivoResource, PlivoResourceInterface
from ..exceptions import *
from ..utils import *

class Brand(PlivoResource):
    _name = 'Brand'
    _identifier_string = 'brand_id'

class Brand(PlivoResourceInterface):
    _resource_type = Brand

    @validate_args(brand_id=[of_type(six.text_type)])
    def get(self, brand_id):
        return self.client.request(
            'GET', ('10dlc','Brand', brand_id), response_type=None)
            
    @validate_args(
        type=[optional(of_type(six.text_type))],
        status=[optional(of_type(six.text_type))])
    def list(self, type=None, status=None):
        return self.client.request(
            'GET', ('10dlc', 'Brand'),
            to_param_dict(self.list, locals()),
            response_type=None,
            objects_type=None)
    
    @validate_args(
        alt_business_id_type=[optional(of_type(six.text_type))],
        alt_business_id=[optional(of_type(six.text_type))],
        city=[optional(of_type(six.text_type))],
        company_name=[optional(of_type(six.text_type))],
        country=[optional(of_type(six.text_type))],
        ein=[optional(of_type(six.text_type))],
        ein_issuing_country=[optional(of_type(six.text_type))],
        email=[optional(of_type(six.text_type))],
        entity_type=[optional(of_type(six.text_type))],
        first_name=[optional(of_type(six.text_type))],
        last_name=[optional(of_type(six.text_type))],
        phone=[optional(of_type(six.text_type))],
        postal_code=[optional(of_type(six.text_type))],
        registration_status=[optional(of_type(six.text_type))],
        state=[optional(of_type(six.text_type))],
        stock_exchange=[optional(of_type(six.text_type))],
        stock_symbol=[optional(of_type(six.text_type))],
        street=[optional(of_type(six.text_type))],
        vertical=[optional(of_type(six.text_type))],
        website=[optional(of_type(six.text_type))],
        secondary_vetting=[optional(of_type(six.text_type))])
    def create(self,
               vertical,
               street,
               stock_symbol,
               stock_exchange,
               state,
               registration_status,
               postal_code,
               phone,
               entity_type,
               email,
               ein_issuing_country,
               ein,
               country,
               company_name,
               city,
               alt_business_id_type=None,
               alt_business_id=None,
               first_name=None,
               last_name=False,
               website=None,
               secondary_vetting=None):
        return self.client.request('POST', ('10dlc', 'Brand'),
                                   to_param_dict(self.create, locals()))