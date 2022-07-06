import json,requests
from plivo.base import (ListResponseObject, PlivoResource,
                        PlivoResourceInterface)
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

    def create(iss:str, auth_token:str, sub:str,nbf:str, exp:str, incoming_allowed:bool, outgoing_allowed:bool, app:str):
        flag = 0
        if(app == ""):
            flag = 1
        url = "https://api-qa.voice.plivodev.com/v1/Account/"+iss+"/JWT/Token"

        if(flag == 1):
            payload = json.dumps({
            "sub": sub,
            "iss": iss,
            "nbf": nbf,
            "exp": exp,
            "per": {
                "voice": {
                "incoming_allow": False,
                "outgoing_allow": False
                }
            }
            })
        else:
            payload = json.dumps({
            "sub": sub,
            "iss": iss,
            "nbf": nbf,
            "exp": exp,
            "per": {
                "voice": {
                "incoming_allow": False,
                "outgoing_allow": False
                }
            },
            "app": app
            })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic TUFNSk01TlRCS01NSkhPVFJNWkQ6TkRBeU5HTTFZelkwTTJVeFkyTmlNak16TVdGbU1qVXlNVGc0TmprNA=='
        }
        print("payload", payload)
        print("headers", headers)
        print("url", url)
        response = requests.request("POST", url, headers=headers,data=payload)
        return response.text