# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import ListResponseObject, PlivoResource, PlivoResourceInterface
from ..exceptions import *
from ..utils import *


class Message(PlivoResource):
    _name = 'Message'
    _identifier_string = 'message_uuid'

    def get(self):
        return self.client.messages.get(self.id)

    def delete(self):
        raise InvalidRequestError('Cannot delete a Message resource')

    def update(self):
        raise InvalidRequestError('Cannot update a Message resource')

    def listMedia(self):
        return self.client.request(
            'GET', ('Message', self.id, 'Media'), response_type=None)


class Messages(PlivoResourceInterface):
    _resource_type = Message

    @validate_args(
        src=[optional(is_phonenumber())],
        dst=[is_iterable(of_type(six.text_type), '<')],
        text=[optional(of_type(six.text_type))],
        type_=[
            optional(all_of(of_type(six.text_type), is_in(('sms', 'mms'))))],
        url=[optional(is_url())],
        method=[optional(of_type(six.text_type))],
        log=[optional(of_type_exact(bool))],
        trackable=[optional(of_type_exact(bool))],
        powerpack_uuid=[optional(of_type(six.text_type))],
        media_urls=[optional(of_type_exact(list))],
        media_ids=[optional(of_type_exact(list))])
    def create(self,
               dst,
               text=None,
               src=None,
               type_='sms',
               url=None,
               method='POST',
               log=True,
               trackable=False,
               powerpack_uuid=None,
               media_urls=None,
               media_ids=None):
        if src in dst.split('<'):
            raise ValidationError(
                'destination number cannot be same as source number')
        elif (src is None) and (powerpack_uuid is None):
            raise ValidationError(
                'Specify either powerpack_uuid or src in request params to send a message'
            )
        elif (src is not None) and (powerpack_uuid is not None):
            raise ValidationError(
                'Both powerpack_uuid and src cannot be specified. Specify either powerpack_uuid or src in request params to send a message.'
            )
        return self.client.request('POST', ('Message', ),
                                   to_param_dict(self.create, locals()))

    @validate_args(message_uuid=[of_type(six.text_type)])
    def get(self, message_uuid):
        return self.client.request(
            'GET', ('Message', message_uuid), response_type=Message)

    @validate_args(
        subaccount=[optional(is_subaccount())],
        message_direction=[optional(is_in(('inbound', 'outbound')))],
        message_time__gt=[optional(is_valid_date())],
        message_time__gte=[optional(is_valid_date())],
        message_time__lt=[optional(is_valid_date())],
        message_time__lte=[optional(is_valid_date())],
        message_time=[optional(is_valid_date())],
        message_state=[
            optional(
                is_in(('queued', 'sent', 'failed', 'delivered', 'undelivered',
                       'rejected')))
        ],
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
             message_direction=None,
             message_time__gt=None,
             message_time__gte=None,
             message_time__lt=None,
             message_time__lte=None,
             message_time=None,
             message_state=None,
             limit=None,
             offset=None,
             error_code=None):
        return self.client.request(
            'GET', ('Message', ),
            to_param_dict(self.list, locals()),
            response_type=ListResponseObject,
            objects_type=Message)
