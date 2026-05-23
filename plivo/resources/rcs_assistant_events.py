# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import PlivoResource, PlivoResourceInterface
from ..exceptions import *
from ..utils import *


class RcsAssistantEvent(PlivoResource):
    _name = 'RcsAssistantEvent'
    _identifier_string = 'api_id'

    def delete(self):
        raise InvalidRequestError('Cannot delete an RcsAssistantEvent resource')

    def update(self):
        raise InvalidRequestError('Cannot update an RcsAssistantEvent resource')


class RcsAssistantEvents(PlivoResourceInterface):
    _resource_type = RcsAssistantEvent

    def create(self, **kwargs):
        return self.client.request(
            'POST', ('RCS', 'AssistantEvents'),
            to_param_dict(self.create, locals()),
        )