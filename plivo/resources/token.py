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
            params = {}
            params['iss'] = iss
            params['per'] = {}
            params['per']['voice'] = {}
            if sub != None:
                params['sub'] = sub
            if nbf != None:
                params['nbf'] = nbf
            if exp != None:
                params['exp'] = exp
            if incoming_allow != None:
                params['per']['voice']['incoming_allow'] = incoming_allow
            if outgoing_allow != None:
                params['per']['voice']['outgoing_allow'] = outgoing_allow
            if app != None:
                params['app'] = app
            return self.client.request('POST', ('JWT','Token', ),params, is_voice_request=True)      
