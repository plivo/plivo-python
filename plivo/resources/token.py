import json
import string
from plivo.base import (ListResponseObject, PlivoResource,PlivoResourceInterface)
from plivo.utils import to_param_dict
from plivo.utils.validators import *

class Token(PlivoResourceInterface):
    @validate_args(
        iss = [required(of_type(six.text_type))],
        sub = [optional(of_type(six.text_type))],
        nbf = [optional(of_type(six.text_type))],
        exp = [optional(of_type(six.text_type))],
        incoming_allow = [optional(of_type(bool,string))],
        outgoing_allow = [optional(of_type(bool,string))],
        app = [optional(of_type(six.text_type))]
    )

    def create( self, iss, sub = None, nbf = None, exp = None, incoming_allow = None, outgoing_allow = None, app = None):    
        if(incoming_allow == True and sub == None):
            raise ValidationError('Sub is required')
        elif(iss == None):
            raise ValidationError('Iss is required')
        else:
            return self.client.request('POST', ('JWT','Token', ),to_param_dict(self.create,locals()), is_voice_request=True)      
