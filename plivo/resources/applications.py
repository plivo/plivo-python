# -*- coding: utf-8 -*-
"""
Application class - along with its list class
"""

from plivo.base import (ListResponseObject, PlivoResource,
                        PlivoResourceInterface)
from plivo.resources.accounts import Subaccount
from plivo.utils import to_param_dict
from plivo.utils.validators import *


class Application(PlivoResource):
    _name = 'Application'
    _identifier_string = 'app_id'

    def update(self,
               answer_url,
               answer_method='POST',
               hangup_url=None,
               hangup_method='POST',
               fallback_answer_url=None,
               fallback_method='POST',
               message_url=None,
               message_method='POST',
               default_number_app=False,
               default_endpoint_app=False,
               subaccount=None,
			   log_incoming_messages=True,
               public_uri=None):
        params = to_param_dict(self.update, locals())
        self.__dict__.update(params)
        return self.client.applications.update(self.id, **params)

    def delete(self, cascade=None, new_endpoint_application=None):
        return self.client.applications.delete(self.id, cascade, new_endpoint_application)

    def get(self):
        resp = self.client.applications.get()
        self.__dict__.update(resp.__dict__)
        return resp


class Applications(PlivoResourceInterface):
    _resource_type = Application

    @validate_args(
        answer_url=[is_url()],
        app_name=[of_type(six.text_type)],
        answer_method=[optional(of_type(six.text_type))],
        hangup_url=[optional(is_url())],
        hangup_method=[optional(of_type(six.text_type))],
        fallback_answer_url=[optional(is_url())],
        fallback_method=[optional(of_type(six.text_type))],
        message_url=[optional(is_url())],
        message_method=[optional(of_type(six.text_type))],
        default_number_app=[optional(of_type_exact(bool))],
        default_endpoint_app=[optional(of_type_exact(bool))],
        subaccount=[optional(is_subaccount())],
        log_incoming_messages=[optional(of_type_exact(bool))],
        public_uri=[optional(of_type_exact(bool))])
    def create(self,
               answer_url,
               app_name,
               answer_method='POST',
               hangup_url=None,
               hangup_method='POST',
               fallback_answer_url=None,
               fallback_method='POST',
               message_url=None,
               message_method='POST',
               default_number_app=False,
               default_endpoint_app=False,
               subaccount=None,
               log_incoming_messages=True,
               public_uri=None):

        if subaccount:
            if isinstance(subaccount, Subaccount):
                subaccount = subaccount.id
        return self.client.request('POST', ('Application', ), to_param_dict(self.create, locals()), is_voice_request=True)

    @validate_args(app_id=[of_type(six.text_type)])
    def get(self, app_id):
        return self.client.request(
            'GET', ('Application', app_id), response_type=Application, is_voice_request=True)

    @validate_args(
        subaccount=[optional(is_subaccount())],
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
    def list(self, subaccount=None, limit=20, offset=0):
        if subaccount:
            if isinstance(subaccount, Subaccount):
                subaccount = subaccount.id
        return self.client.request(
            'GET', ('Application', ),
            to_param_dict(self.list, locals()),
            response_type=ListResponseObject,
            objects_type=Application, is_voice_request=True)

    @validate_args(
        answer_url=[is_url()],
        app_id=[of_type(six.text_type)],
        answer_method=[optional(of_type(six.text_type))],
        hangup_url=[optional(is_url())],
        hangup_method=[optional(of_type(six.text_type))],
        fallback_answer_url=[optional(is_url())],
        fallback_method=[optional(of_type(six.text_type))],
        message_url=[optional(is_url())],
        message_method=[optional(of_type(six.text_type))],
        default_number_app=[optional(of_type_exact(bool))],
        default_endpoint_app=[optional(of_type_exact(bool))],
        subaccount=[optional(is_subaccount())],
        log_incoming_messages=[optional(of_type_exact(bool))],
        public_uri=[optional(of_type_exact(bool))])
    def update(self,
               app_id,
               answer_url,
               answer_method='POST',
               hangup_url=None,
               hangup_method='POST',
               fallback_answer_url=None,
               fallback_method='POST',
               message_url=None,
               message_method='POST',
               default_number_app=False,
               default_endpoint_app=False,
               subaccount=None,
               log_incoming_messages=True,
               public_uri=None):
        if subaccount:
            if isinstance(subaccount, Subaccount):
                subaccount = subaccount.id
        return self.client.request('POST', ('Application', app_id),
                                   to_param_dict(self.update, locals()), is_voice_request=True)

    @validate_args(
        app_id=[of_type(six.text_type)],
        new_endpoint_application=[optional(of_type(six.text_type))],
        cascade=[optional(of_type_exact(bool))]
    )
    def delete(self, app_id, cascade=None, new_endpoint_application=None):
        return self.client.request('DELETE', ('Application', app_id),
                                   to_param_dict(self.delete, locals()), is_voice_request=True)
