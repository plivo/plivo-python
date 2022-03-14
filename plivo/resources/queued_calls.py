from plivo.base import PlivoResource, PlivoResourceInterface

from ..utils.validators import *


class QueuedCall(PlivoResource):
    _name = 'QueuedCall'
    _identifier_string = 'call_uuid'


class QueuedCalls(PlivoResourceInterface):
    _resource_type = QueuedCall
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
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],)
    def list_ids(self, limit=20, offset=0, callback_url=None, callback_method=None):
        return self.client.request('GET', ('Call', ), {
            'status': 'queued',
            'limit': limit,
            'offset': offset,
            'callback_url': callback_url,
            'callback_method': callback_method
        }, is_voice_request=True)

    @validate_args(_id=[of_type(six.text_type)],
                   callback_url=[optional(is_url())],
                   callback_method=[optional(of_type(six.text_type))],)
    def get(self,
            _id,
            callback_url=None,
            callback_method=None):
        local_object={}
        local_object['status'] = 'queued'
        if callback_url:
            local_object['callback_url'] = callback_url
        if callback_method:
            local_object['callback_method'] = callback_method

        return self.client.request('GET', ('Call', _id), local_object, is_voice_request=True)
