# -*- coding: utf-8 -*-
from plivo.base import PlivoResourceInterface, ResponseObject


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
            ('Lookup/Number', number),
            data=params,
            response_type=Number,
            plivo_api_v1_base_url=True)
