# -*- coding: utf-8 -*-
from plivo.base import PlivoResourceInterface, ResponseObject


LOOKUP_API_ENDPOINT = "https://lookup.plivo.com/v1/Number"


class Number(ResponseObject):
    def __init__(self, client, data):
        super(Number, self).__init__(data)


class Lookup(PlivoResourceInterface):
    _resource_type = Number

    def get(self, number, info_type='carrier'):
        params = {
            'type': info_type,
        }
        return self.client.request(
            'GET',
            (LOOKUP_API_ENDPOINT, number),
            data=params,
            response_type=Number,
            is_lookup_request=True)
