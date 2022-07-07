import json
from plivo.base import (ListResponseObject, PlivoResource,PlivoResourceInterface)
from plivo.utils import to_param_dict
from plivo.utils.validators import *

class Token(PlivoResourceInterface):
    @validate_args(
        iss = [required(of_type(six.text_type))],
        auth_token = [required(of_type(six.text_type))],
        sub = [optional(of_type(six.text_type))],
        nbf = [required(of_type(six.text_type))],
        exp = [required(of_type(six.text_type))],
        incoming_allowed = [optional(of_type(bool))],
        outgoing_allowed = [optional(of_type(bool))],
        app = [optional(of_type(six.text_type))]
    )

    def create( self,iss, auth_token, sub,nbf, exp, incoming_allowed, outgoing_allowed,app):
        if(incoming_allowed == True and sub == None):
                raise ValidationError('Subaccount is required')
        else:
            payload = json.dumps({
                "sub": sub,
                "iss": iss,
                "nbf": nbf,
                "exp": exp,
                "per": {
                "voice": {
                "incoming_allow": incoming_allowed,
                "outgoing_allow": outgoing_allowed
                    }
                },
                "app": app
            })
            return self.client.request('POST', ('JWT/Token', ), to_param_dict(self.create, locals()), is_voice_request=True)
