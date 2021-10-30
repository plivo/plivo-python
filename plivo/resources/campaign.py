# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import ListResponseObject, PlivoResource, PlivoResourceInterface
from ..exceptions import *
from ..utils import *

class Campaign(PlivoResource):
    _name = 'Campaign'
    _identifier_string = 'campaign_id'

class Campaign(PlivoResourceInterface):
    _resource_type = Campaign

    @validate_args(campaign_id=[of_type(six.text_type)])
    def get(self, campaign_id):
        return self.client.request(
            'GET', ('10dlc','Campaign', campaign_id), response_type=None)

    @validate_args(
        brand=[optional(of_type(six.text_type))],
        usecase=[optional(of_type(six.text_type))])
    def list(self, brand=None, usecase=None):
        return self.client.request(
            'GET', ('10dlc', 'Campaign'),
            to_param_dict(self.list, locals()),
            response_type=None,
            objects_type=None)
    
    @validate_args(
        brand_id=[optional(of_type(six.text_type))],
        campaign_alias=[optional(of_type(six.text_type))],
        vertical=[optional(of_type(six.text_type))],
        usecase=[optional(of_type(six.text_type))],
        description=[optional(of_type(six.text_type))],
        embedded_link=[optional(of_type_exact(bool))],
        embedded_phone=[optional(of_type_exact(bool))],
        age_gated=[optional(of_type_exact(bool))],
        direct_lending=[optional(of_type_exact(bool))],
        subscriber_optin=[optional(of_type_exact(bool))],
        subscriber_optout=[optional(of_type_exact(bool))],
        subscriber_help=[optional(of_type_exact(bool))],
        sample1=[optional(of_type(six.text_type))],
        sample2=[optional(of_type(six.text_type))])
    def create(self,
               brand_id,
               vertical,
               usecase,
               description,
               sample1,
               sample2,
               embedded_link=False,
               embedded_phone=False,
               age_gated=False,
               direct_lending=False,
               subscriber_optout=True,
               subscriber_optin=True,
               subscriber_help=True,
               campaign_alias=None,
               sub_usecases=None):
        return self.client.request('POST', ('10dlc', 'Campaign'),
                                   to_param_dict(self.create, locals()))