# -*- coding: utf-8 -*-
from plivo.base import PlivoResource, PlivoResourceInterface, ResponseObject
from plivo.utils import to_param_dict
from plivo.utils.validators import *


class VerifyAppTemplate(ResponseObject):
    def __init__(self, dct):
        super(VerifyAppTemplate, self).__init__(dct)


class VerifyAppTemplatesResponse(ResponseObject):
    def __init__(self, client, dct):
        super(VerifyAppTemplatesResponse, self).__init__(dct)
        self.api_id = dct.get('api_id', None)
        self.templates = dct.get('templates', [])

    def __iter__(self):
        if self.templates is not None:
            return iter(self.templates)
        return iter([])

    def __len__(self):
        if self.templates is not None:
            return len(self.templates)
        return 0

    def __str__(self):
        import pprint
        return pprint.pformat({'api_id': self.api_id, 'templates': self.templates})

    def __repr__(self):
        return self.__str__()


class VerifyAppTemplates(PlivoResourceInterface):
    def list(self):
        return self.client.request(
            'GET',
            ('Verify', 'App', 'templates'),
            response_type=VerifyAppTemplatesResponse,
        )