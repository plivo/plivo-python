# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import PlivoResource, PlivoResourceInterface
from ..exceptions import *
from ..utils import *


class BulkMessage(PlivoResource):
    _name = 'BulkMessage'
    _identifier_string = 'message_uuid'

    def delete(self):
        raise InvalidRequestError('Cannot delete a BulkMessage resource')

    def update(self):
        raise InvalidRequestError('Cannot update a BulkMessage resource')


class BulkMessages(PlivoResourceInterface):
    _resource_type = BulkMessage

    @validate_args(
        src=[of_type(six.text_type)],
        dst=[is_iterable(of_type(six.text_type), '<')],
        text=[of_type(six.text_type)],
        type_=[optional(of_type(six.text_type))],
        url=[optional(is_url())],
        method=[optional(of_type(six.text_type))],
        log=[optional(of_type_exact(bool))],
        powerpack_uuid=[optional(of_type(six.text_type))],
    )
    def create(self,
               src,
               dst,
               text,
               type_=None,
               url=None,
               method=None,
               log=None,
               powerpack_uuid=None):
        params = to_param_dict(self.create, locals())
        # rename type_ -> type for API
        if 'type_' in params:
            params['type'] = params.pop('type_')
        return self.client.request('POST', ('Message', 'Bulk'),
                                   params)