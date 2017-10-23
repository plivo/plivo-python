# -*- coding: utf-8 -*-
from plivo.base import PlivoResource, PlivoResourceInterface

from ..utils.validators import *


class LiveCall(PlivoResource):
    _name = 'LiveCall'
    _identifier_string = 'call_uuid'


class LiveCalls(PlivoResourceInterface):
    _resource_type = LiveCall
    _iterable = False

    @validate_args(
        limit=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(
                        lambda limit: 0 < limit <= 20,
                        message='0 < limit <= 20')))
        ],
        offset=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda offset: 0 <= offset, message='0 <= offset')))
        ])
    def list_ids(self, limit=20, offset=0):
        return self.client.request('GET', ('Call', ), {
            'status': 'live',
            'limit': limit,
            'offset': offset,
        })

    @validate_args(_id=[of_type(six.text_type)])
    def get(self, _id):
        return self.client.request('GET', ('Call', _id), {'status': 'live'})
