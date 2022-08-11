import string

from plivo.base import (PlivoResourceInterface)
from plivo.utils.validators import *


class Token(PlivoResourceInterface):
    @validate_args(
        iss=[required(of_type(six.text_type))],
        sub=[optional(of_type(six.text_type))],
        nbf=[optional(of_type(six.text_type))],
        exp=[optional(of_type(six.text_type))],
        incoming_allow=[optional(of_type(bool, string))],
        outgoing_allow=[optional(of_type(bool, string))],
        app=[optional(of_type(six.text_type))]
    )
    def create(self, iss, sub=None, nbf=None, exp=None, incoming_allow=None, outgoing_allow=None, app=None):
        if incoming_allow is True and sub is None:
            raise ValueError('sub is required when incoming_allow is true')
        else:
            params = {'iss': iss}

            if sub:
                params['sub'] = sub
            if nbf:
                params['nbf'] = nbf
            if exp:
                params['exp'] = exp
            if incoming_allow or outgoing_allow:
                params['per'] = {}
                params['per']['voice'] = {}
                if incoming_allow:
                    params['per']['voice']['incoming_allow'] = incoming_allow
                if outgoing_allow:
                    params['per']['voice']['outgoing_allow'] = outgoing_allow
            if app:
                params['app'] = app

            return self.client.request('POST', ('JWT', 'Token',), params, is_voice_request=True)
