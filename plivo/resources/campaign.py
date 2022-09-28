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
        usecase=[optional(of_type(six.text_type))],
        limit=[optional(of_type(*six.integer_types))],
        offset=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda offset: 0 <= offset, '0 <= offset')))
        ])
    def list(self, brand=None, usecase=None, 
                limit=None, offset=None):
        return self.client.request(
            'GET', ('10dlc', 'Campaign', ),
            to_param_dict(self.list, locals()),
            response_type=None,
            objects_type=None)
    
    @validate_args(
        brand_id=[required(of_type(six.text_type))],
        campaign_alias=[optional(of_type(six.text_type))],
        vertical=[required(of_type(six.text_type))],
        usecase=[required(of_type(six.text_type))],
        description=[optional(of_type(six.text_type))],
        embedded_link=[optional(of_type_exact(bool))],
        embedded_phone=[optional(of_type_exact(bool))],
        age_gated=[optional(of_type_exact(bool))],
        direct_lending=[optional(of_type_exact(bool))],
        subscriber_optin=[optional(of_type_exact(bool))],
        subscriber_optout=[optional(of_type_exact(bool))],
        subscriber_help=[optional(of_type_exact(bool))],
        affiliate_marketing=[optional(of_type_exact(bool))],
        sample1=[optional(of_type(six.text_type))],
        sample2=[optional(of_type(six.text_type))],
        sample3=[optional(of_type(six.text_type))],
        sample4=[optional(of_type(six.text_type))],
        sample5=[optional(of_type(six.text_type))],
        message_flow=[optional(of_type(six.text_type))],
        help_message=[optional(of_type(six.text_type))],
        optin_keywords=[optional(of_type(six.text_type))],
        optin_message=[optional(of_type(six.text_type))],
        optout_keywords=[optional(of_type(six.text_type))],
        optout_message=[optional(of_type(six.text_type))],
        help_keywords=[optional(of_type(six.text_type))],
        url=[optional(of_type(six.text_type))],
        method=[optional(of_type(six.text_type))])
    def create(self,
               brand_id,
               vertical,
               usecase,
               description='',
               sample1='',
               sample2='',
               sample3='',
               sample4='',
               sample5='',
               url='',
               message_flow='',
               help_message='',
               optin_keywords='',
               optin_message='',
               optout_keywords='',
               optout_message='',
               help_keywords='',
               method='POST',
               embedded_link=False,
               embedded_phone=False,
               age_gated=False,
               direct_lending=False,
               subscriber_optout=False,
               subscriber_optin=False,
               subscriber_help=False,
               affiliate_marketing=False,
               campaign_alias=None,
               sub_usecases=[]):
        return self.client.request('POST', ('10dlc', 'Campaign'),
                                   to_param_dict(self.create, locals()))


    @validate_args(
        campaign_id=[required(of_type(six.text_type))],
        url=[optional(of_type(six.text_type))],
        method=[optional(of_type(six.text_type))],
    )
    def number_link(self,
                    campaign_id,
                    url='',
                    method='POST',
                    numbers=[]):
        return self.client.request('POST', ('10dlc', 'Campaign',  campaign_id, 'Number'),
                                   to_param_dict(self.number_link, locals()))

    @validate_args(
        campaign_id=[of_type(six.text_type)],
        limit=[optional(of_type(*six.integer_types))],
        offset=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda offset: 0 <= offset, '0 <= offset')))
        ])
    def get_numbers(self,
                    campaign_id,
                    limit=None, 
                    offset=None):
        params ={}
        if limit:
            params['limit']= limit
        if offset:
            params['offset'] = offset
        return self.client.request('GET', ('10dlc', 'Campaign',  campaign_id, 'Number'),
                                   params, to_param_dict(self.create, locals()))

    @validate_args(
        campaign_id=[of_type(six.text_type)],
        number=[of_type(six.text_type)])
    def get_number(self,
                campaign_id,
                number):
        return self.client.request('GET', ('10dlc', 'Campaign',  campaign_id, 'Number', number),
                                   to_param_dict(self.create, locals()))

    @validate_args(
        campaign_id=[of_type(six.text_type)],
        number=[of_type(six.text_type)])
    def number_unlink(self,
                campaign_id,
                number,
                url='',
                method='POST'
                ):
        return self.client.request('DELETE', ('10dlc', 'Campaign',  campaign_id, 'Number', number),
                                   to_param_dict(self.create, locals()))