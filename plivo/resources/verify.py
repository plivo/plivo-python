# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import ListResponseObject, PlivoResource, PlivoResourceInterface, ListSessionResponseObject
from ..exceptions import *
from ..utils import *


class Session(PlivoResource):
    _name = 'Session'
    _identifier_string = 'session_uuid'

    def delete(self):
        raise InvalidRequestError('Cannot delete a Session resource')

    def update(self):
        raise InvalidRequestError('Cannot update a Session resource')


class Sessions(PlivoResourceInterface):
    _resource_type = Session

    @validate_args(
        app_uuid=[optional(of_type(six.text_type))],
        otp=[optional(of_type(six.text_type))],
        recipient=[required(is_phonenumber())],
        channel=[optional(all_of(of_type(six.text_type), is_in(('sms', 'voice'))))],
        url=[optional(is_url())],
        method=[optional(of_type(six.text_type))],
        locale=[optional(of_type(six.text_type))])
    def create(self,
               app_uuid=None,
               otp=None,
               recipient=None,
               channel=None,
               url=None,
               method='POST',
               locale=None,
               brand_name=None,
               app_hash=None,
               code_length=None,
               dtmf=None,
               fraud_check=None):
        if recipient is None:
            raise ValidationError('destination number is required')
        return self.client.request('POST', ('Verify', 'Session', ),
                                   to_param_dict(self.create, locals()))

    @validate_args(session_uuid=[of_type(six.text_type)])
    def get(self, session_uuid):
        return self.client.request(
            'GET', ('Verify', 'Session', session_uuid), response_type=Session)

    @validate_args(
        subaccount=[optional(is_subaccount())],
        status=[optional(is_in(('in-progress', 'expired', 'verified')))],
        session_time__gt=[optional(is_valid_date())],
        session_time__gte=[optional(is_valid_date())],
        session_time__lt=[optional(is_valid_date())],
        session_time__lte=[optional(is_valid_date())],
        session_time=[optional(is_valid_date())],
        country=[optional(of_type(six.text_type))],
        alias=[optional(of_type(six.text_type))],
        app_uuid=[optional(of_type(six.text_type))],
        recipient=[optional(of_type(six.text_type))],
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
    def list(self,
             subaccount=None,
             status=None,
             session_time__gt=None,
             session_time__gte=None,
             session_time__lt=None,
             session_time__lte=None,
             session_time=None,
             country=None,
             alias=None,
             app_uuid=None,
             recipient=None,
             limit=None,
             offset=None,
             brand_name=None,
             app_hash=None):
        return self.client.request(
            'GET', ('Verify', 'Session', ),
            to_param_dict(self.list, locals()),
            response_type=ListSessionResponseObject,
            objects_type=Session)

    @validate_args(
        otp=[optional(of_type(six.text_type))],
        session_uuid=[of_type(six.text_type)]
    )
    def validate(self, session_uuid, otp=None):
        return self.client.request('POST', ('Verify', 'Session', session_uuid),
                                   to_param_dict(self.validate, locals()))

