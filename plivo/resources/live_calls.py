# -*- coding: utf-8 -*-
from plivo.base import PlivoResource,\
    PlivoResourceInterface
from plivo.utils import to_param_dict
from ..utils.validators import *
from plivo.utils import to_param_dict


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
        ],
        call_direction=[
            optional(of_type(six.text_type), is_in(('inbound', 'outbound')))
        ],
        from_number=[optional(is_phonenumber())],
        to_number=[optional(is_iterable(of_type(six.text_type), sep='<'))],
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def list_ids(self,
                 call_direction=None,
                 from_number=None,
                 to_number=None,
                 limit=20,
                 offset=0,
                 callback_url=None,
                 callback_method=None
                 ):
        params = to_param_dict(self.list_ids, locals())
        params.update({'status': 'live'})
        return self.client.request('GET', ('Call',), params, is_voice_request=True)

    @validate_args(_id=[of_type(six.text_type)],
                   callback_url=[optional(is_url())],
                   callback_method=[optional(of_type(six.text_type))])
    def get(self,
            _id,
            callback_url=None,
            callback_method=None):
        local_object = {}
        local_object['status'] = 'live'
        if callback_url:
            local_object['callback_url'] = callback_url
        if callback_method:
            local_object['callback_method'] = callback_method
        return self.client.request(
            'GET', ('Call', _id), local_object, is_voice_request=True
        )
