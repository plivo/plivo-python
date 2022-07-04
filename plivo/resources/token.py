import numbers
from this import s
import jwt
import time
import sys,json,requests
from plivo.base import (ListResponseObject, PlivoResource,
                        PlivoResourceInterface)
from plivo.utils import to_param_dict
from plivo.utils.validators import *


class Token(PlivoResourceInterface):
    @validate_args(
        sub = [optional(of_type(six.text_type))],
        iss = [optional(of_type(six.text_type))],
        nbf = [optional(of_type(numbers))],
        exp = [optional(of_type(numbers))], 
        per = [
            all_of(
                of_type(six.text_type),
                is_in(('voice','incoming_allow', 'outgoing_allow')))
        ],
        incoming_allowed = [optional(of_type_exact(bool))],
        outgoing_allowed = [optional(of_type_exact(bool))],
        app = [optional(of_type(six.text_type))],
        auth_id = [required(of_type(six.text_type))],


    )
    def create(self, iss:str, sub:str,nbf:str, exp:str, incoming_allowed:bool, outgoing_allowed:bool, app:str):
        url = "https://api-qa.voice.plivodev.com/v1/Account/"+iss+"/JWT/Token"
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
        headers = {
           'authorization': 'Basic TUFNRFZMWkpZMlpHWTVNV1UxWko6WlRKaU9EYzVNVE0xT0RBM016TXlZbVk0TlRBd1l6QTNNamMyT1dOaA==',
           'cache-control': 'no-cache',
           'content-type': 'application/json',
           'postman-token': '6a4ab3a7-cb2d-a410-fc39-220af5712d23'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text


    