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
        status=[optional(of_type(six.text_type))],
        limit=[optional(of_type(*six.integer_types))],
        offset=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda offset: 0 <= offset, '0 <= offset')))
        ])
    def list(self, type=None, status=None, 
                limit=None, offset=None):
        return self.client.request(
            'GET', ('10dlc', 'Brand', ),
            to_param_dict(self.list, locals()),
            response_type=None,
            objects_type=None)
    
    @validate_args(
        brand_alias=[required(of_type(six.text_type))],
        brand_type=[optional(of_type(six.text_type), is_in(('STANDARD','STARTER')))],
        profile_uuid=[required(of_type(six.text_type))],
        secondary_vetting=[optional(of_type_exact(bool))],
        url=[optional(of_type(six.text_type))],
        method=[optional(of_type(six.text_type))])
    def create(self,
               brand_alias,
               brand_type,
               profile_uuid,
               secondary_vetting=False,
               url='',
               method='POST'
        ):
        return self.client.request('POST', ('10dlc', 'Brand'),
                                   to_param_dict(self.create, locals()))