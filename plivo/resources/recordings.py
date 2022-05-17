# -*- coding: utf-8 -*-
"""
Recording class - along with its list class
"""

from plivo.base import (ListResponseObject, PlivoResource,
                        PlivoResourceInterface)
from plivo.resources.accounts import Subaccount
from plivo.utils import is_valid_time_comparison, to_param_dict
from plivo.utils.validators import *


class Recording(PlivoResource):
    _name = 'Recording'
    _identifier_string = 'recording_id'

    def delete(self):
        return self.client.recordings.delete(self.id)


class Recordings(PlivoResourceInterface):
    _resource_type = Recording

    @validate_args(
        from_number=[optional(of_type(six.text_type))],
        to_number=[optional(of_type(six.text_type))],
        conference_name=[optional(of_type(six.text_type))],
        mpc_name=[optional(of_type(six.text_type))],
        conference_uuid=[optional(of_type(six.text_type))],
        mpc_uuid=[optional(of_type(six.text_type))],
        subaccount=[optional(is_subaccount())],
        call_uuid=[optional(of_type(six.text_type))],
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
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def list(self,
             subaccount=None,
             call_uuid=None,
             add_time__gt=None,
             add_time__gte=None,
             add_time__lt=None,
             add_time__lte=None,
             add_time=None,
             limit=20,
             offset=0,
             callback_url=None,
             callback_method=None,
             from_number=None,
             to_number=None,
             conference_name=None,
             mpc_name=None,
             conference_uuid=None,
             mpc_uuid=None):

        if subaccount:
            if isinstance(subaccount, Subaccount):
                subaccount = subaccount.id

        if add_time__gt and is_valid_time_comparison(add_time__gt):
            add_time__gt = str(add_time__gt)

        if add_time__gte and is_valid_time_comparison(add_time__gte):
            add_time__gte = str(add_time__gte)

        if add_time__lt and is_valid_time_comparison(add_time__lt):
            add_time__lt = str(add_time__lt)

        if add_time__lte and is_valid_time_comparison(add_time__lte):
            add_time__lte = str(add_time__lte)

        if add_time and is_valid_time_comparison(add_time):
            add_time = str(add_time)

        if not callback_url:
            return self.client.request(
                'GET',
                ('Recording',),
                to_param_dict(self.list, locals()),
                objects_type=Recording,
                response_type=ListResponseObject,
                is_voice_request=True
            )
        else:
            return self.client.request(
                'GET',
                ('Recording',),
                to_param_dict(self.list, locals()),
                objects_type=Recording,
                is_voice_request=True
            )


    @validate_args(recording_id=[of_type(six.text_type)],
                   callback_url=[optional(is_url())],
                   callback_method=[optional(of_type(six.text_type))],
                   )
    def get(self, recording_id, callback_url=None, callback_method=None):
        if not callback_url:
            return self.client.request(
                'GET', ('Recording', recording_id), response_type=Recording, is_voice_request=True)
        else:
            return self.client.request(
                'GET', ('Recording', recording_id), to_param_dict(self.get, locals()), is_voice_request=True)

    @validate_args(
        recording_id=[of_type(six.text_type)],
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def delete(self, recording_id, callback_url=None, callback_method=None):
        return self.client.request('DELETE', ('Recording', recording_id),
                                   to_param_dict(self.delete, locals()), is_voice_request=True)
