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
        ])
    def list_ids(self, limit=20, offset=0):
        return self.client.request('GET', ('Call', ), {
            'status': 'queued',
            'limit': limit,
            'offset': offset,
        }, is_voice_request=True)

    @validate_args(_id=[of_type(six.text_type)])
    def get(self, _id):
        return self.client.request('GET', ('Call', _id), {'status': 'queued'}, is_voice_request=True)
