# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import ListResponseObject, PlivoResource, PlivoResourceInterface
from ..exceptions import *
from ..utils import *

class Profile(PlivoResource):
    _name = 'Profile'
    _identifier_string = 'Profile_uuid'

class Profile(PlivoResourceInterface):
    _resource_type = Profile

    @validate_args(profile_uuid=[of_type(six.text_type)])
    def get(self, profile_uuid):
        return self.client.request(
            'GET', ('Profile', profile_uuid), response_type=None)

    @validate_args(
        limit=[optional(of_type(*six.integer_types))],
        offset=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda offset: 0 <= offset, '0 <= offset')))
        ])
    def list(self, limit=None, offset=None):
        params ={}
        if limit:
            params['limit']= limit
        if offset:
            params['offset'] = offset

        return self.client.request(
            'GET', ('Profile', ), params,
            response_type=None,
            objects_type=None)

    @validate_args(profile_uuid=[of_type(six.text_type)])
    def delete(self, profile_uuid):
        return self.client.request(
            'DELETE', ('Profile', profile_uuid),
            response_type=None,
            objects_type=None)
    
    @validate_args(
        profile_alias=[optional(of_type(six.text_type))],
        customer_type=[required(of_type(six.text_type))],
        entity_type=[required(of_type(six.text_type))],
        company_name=[required(of_type(six.text_type))],
        ein=[optional(of_type(six.text_type))],
        ein_issuing_country=[optional(of_type(six.text_type))],
        stock_symbol=[optional(of_type(six.text_type))],
        stock_exchange=[optional(of_type(six.text_type))],
        website=[optional(of_type(six.text_type))],
        vertical=[required(of_type(six.text_type))],
        alt_business_id=[optional(of_type(six.text_type))],
        alt_business_id_type=[optional(of_type(six.text_type))],
        plivo_subaccount=[optional(of_type(six.text_type))],
        address=[optional(of_type_exact(dict))],
        authorized_contact=[optional(of_type_exact(dict))])
    def create(self,
               profile_alias,
               customer_type,
               entity_type,
               company_name,
               vertical,
               alt_business_id='',
               alt_business_id_type= '',
               plivo_subaccount='',
               ein='',
               ein_issuing_country='',
               stock_symbol='',
               stock_exchange='',
               website='',
               address={},
               authorized_contact={}):
        return self.client.request('POST', ('Profile', ),
                                   to_param_dict(self.create, locals()))


    # params values should be dictionary like 
    # {'address': {}, 'authorized_contact': {}, 'entity_type':'', 'vertical': '', 'company_name': '', 'website':''} 
    def update(self,profile_uuid, params=None):
        if params == None:
            raise ValidationError(
                'required atleast one of powerpack attributes'
            )
        return self.client.request('POST', ('Profile', profile_uuid), params)
