# -*- coding: utf-8 -*-
from plivo.utils import to_param_dict
from plivo.utils.validators import *

from ..base import ListResponseObject, PlivoResource, PlivoResourceInterface


class Endpoint(PlivoResource):
    _name = 'Endpoint'
    _identifier_string = 'endpoint_id'

    @validate_args(
        password=[of_type(six.text_type)],
        alias=[of_type(six.text_type)],
        app_id=[optional(of_type(six.text_type))])
    def update(self, password=None, alias=None, app_id=None):
        params = to_param_dict(self.update, locals())
        self.__dict__.update(params)
        return self.client.endpoints.update(self.id, **params)

    def delete(self):
        return self.client.endpoints.delete(self.id)


class Endpoints(PlivoResourceInterface):
    _resource_type = Endpoint

    @validate_args(
        username=[of_type(six.text_type)],
        password=[of_type(six.text_type)],
        alias=[of_type(six.text_type)],
        app_id=[optional(of_type(six.text_type))])
    def create(self, username, password, alias, app_id=None):
        return self.client.request('POST', ('Endpoint', ),
                                   to_param_dict(self.create, locals()), is_voice_request=True)

    @validate_args(endpoint_id=[of_type(six.text_type)])
    def get(self, endpoint_id):
        return self.client.request('GET', ('Endpoint', endpoint_id), is_voice_request=True)

    @validate_args(
        limit=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda limit: 0 < limit <= 20, '0 < limit <= 20')))
                ],
        offset=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda offset: 0 <= offset, '0 <= offset')))
        ])
    def list(self, limit=20, offset=0):
        return self.client.request(
            'GET',
            ('Endpoint', ),
            to_param_dict(self.list, locals()),
            objects_type=Endpoint,
            response_type=ListResponseObject, is_voice_request=True)

    @validate_args(
        endpoint_id=[of_type(six.text_type)],
        password=[optional(of_type(six.text_type))],
        alias=[optional(of_type(six.text_type))],
        app_id=[optional(of_type(six.text_type))])
    def update(self, endpoint_id, password=None, alias=None, app_id=None):
        return self.client.request('POST', ('Endpoint', endpoint_id),
                                   to_param_dict(self.update, locals()), is_voice_request=True)

    @validate_args(endpoint_id=[of_type(six.text_type)])
    def delete(self, endpoint_id):
        return self.client.request('DELETE', ('Endpoint', endpoint_id), is_voice_request=True)
