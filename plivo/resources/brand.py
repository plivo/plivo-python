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
        brand_alias=[required(of_type(six.text_type))],
        brand_type=[optional(of_type(six.text_type), is_in(('STANDARD','STARTER')))],
        profile_uuid=[required(of_type(six.text_type))],
        secondary_vetting=[optional(of_type_exact(bool))],
        url=[optional(of_type(six.text_type))],
        method=[optional(of_type(six.text_type))],
        subaccount_id=[optional(of_type(six.text_type))],
        emailRecipients=[optional(of_type(six.text_type))],
        campaignName=[optional(of_type(six.text_type))],
        campaignUseCase=[optional(of_type(six.text_type))],
        campaignDescription=[optional(of_type(six.text_type))],
        sampleMessage1=[optional(of_type(six.text_type))],
        sampleMessage2=[optional(of_type(six.text_type))],
        embeddedLink=[optional(of_type_exact(bool))],
        embeddedPhone=[optional(of_type_exact(bool))],
        numberPool=[optional(of_type_exact(bool))],
        ageGated=[optional(of_type_exact(bool))],
        directLending=[optional(of_type_exact(bool))],
        subscriberOptin=[optional(of_type_exact(bool))],
        subscriberOptout=[optional(of_type_exact(bool))],
        subscriberHelp=[optional(of_type_exact(bool))],
        affiliateMarketing=[optional(of_type_exact(bool))],
        resellerID=[optional(of_type(six.text_type))])
    def create(self,
               brand_alias,
               brand_type,
               profile_uuid,
               secondary_vetting=False,
               url='',
               method='POST',
               subaccount_id='',
               emailRecipients='',
               campaignName='',
               campaignUseCase='',
               campaignSubUseCases=[],
               campaignDescription='',
               sampleMessage1='',
               sampleMessage2='',
               embeddedLink=False,
               embeddedPhone=False,
               numberPool=False,
               ageGated=False,
               directLending=False,
               subscriberOptin=False,
               subscriberOptout=False,
               subscriberHelp=False,
               affiliateMarketing=False,
               resellerID=''):
        return self.client.request('POST', ('10dlc', 'Brand'),
                                   to_param_dict(self.create, locals()))