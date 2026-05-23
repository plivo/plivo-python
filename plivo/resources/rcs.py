# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import PlivoResource, PlivoResourceInterface, ResponseObject
from ..exceptions import *
from ..utils import *


class RcsCapabilityResponse(ResponseObject):
    def __init__(self, client, dct):
        super(RcsCapabilityResponse, self).__init__(dct)
        self.api_id = dct.get('api_id', None)
        self.phone_number = dct.get('phone_number', None)
        self.is_capable = dct.get('is_capable', None)
        self.features = dct.get('features', None)
        self.message = dct.get('message', None)
        self.error = dct.get('error', None)


class RcsCapability(PlivoResourceInterface):
    @validate_args(
        phone_number=[of_type(six.text_type)],
        agent_uuid=[optional(of_type(six.text_type))],
    )
    def check(self, phone_number, agent_uuid=None):
        return self.client.request(
            'GET',
            ('RCS', 'Capability'),
            to_param_dict(self.check, locals()),
            response_type=RcsCapabilityResponse,
        )