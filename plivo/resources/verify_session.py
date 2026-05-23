# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import PlivoResource, PlivoResourceInterface, ListSessionResponseObject
from ..exceptions import *
from ..utils import *


class VerifySession(PlivoResource):
    _name = 'VerifySession'
    _identifier_string = 'session_uuid'

    def get(self):
        return self.client.verify_session.get(self.id)


class VerifySessions(PlivoResourceInterface):
    _resource_type = VerifySession

    @validate_args(
        app_hash=[optional(of_type(six.text_type))],
        brand_name=[optional(of_type(six.text_type))],
        code_length=[optional(of_type(*six.integer_types))],
        dlt_entity_id=[optional(of_type(six.text_type))],
        dlt_sender_id=[optional(of_type(six.text_type))],
        dlt_template_category=[optional(of_type(six.text_type))],
        dlt_template_id=[optional(of_type(six.text_type))],
        dlt_text=[optional(of_type(six.text_type))],
        dtmf=[optional(of_type(*six.integer_types))],
        fraud_check=[optional(of_type(six.text_type))],
        text=[optional(of_type(six.text_type))],
    )
    def create(self,
               app_hash=None,
               brand_name=None,
               code_length=None,
               dlt_entity_id=None,
               dlt_sender_id=None,
               dlt_template_category=None,
               dlt_template_id=None,
               dlt_text=None,
               dtmf=None,
               fraud_check=None,
               text=None):
        return self.client.request(
            'POST', ('Verify', 'Session'),
            to_param_dict(self.create, locals()))

    @validate_args(session_uuid=[of_type(six.text_type)])
    def get(self, session_uuid):
        return self.client.request(
            'GET', ('Verify', 'Session', session_uuid),
            response_type=VerifySession)

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
        ],
    )
    def list(self,
             limit=None,
             offset=None):
        return self.client.request(
            'GET', ('Verify', 'Session'),
            to_param_dict(self.list, locals()),
            response_type=ListSessionResponseObject,
            objects_type=VerifySession)