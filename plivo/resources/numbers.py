# -*- coding: utf-8 -*-
"""
Number & PhoneNumber classes - along with their list classes
"""

from plivo.base import (ListResponseObject, PlivoResource,
                        PlivoResourceInterface)
from plivo.utils import to_param_dict
from plivo.utils.validators import *


class Number(PlivoResource):
    _name = 'Number'
    _identifier_string = 'number'

    def delete(self):
        return self.client.numbers.delete(self.id)

    def update(self,
               app_id=None,
               subaccount=None,
               alias=None,
               verification_info=None):
        return self.client.numbers.update(self.id, app_id, subaccount, alias,
                                          verification_info)


class Numbers(PlivoResourceInterface):
    def __init__(self, client):
        self._resource_type = Number
        super(Numbers, self).__init__(client)

    @validate_args(
        number=[is_phonenumber()],
        app_id=[optional(of_type(six.text_type))],
        verification_info=[optional(of_type_exact(dict))])
    def buy(self, number, app_id=None, verification_info=None):
        return self.client.request('POST', ('PhoneNumber', number),
                                   to_param_dict(self.buy, locals()))

    def search(self,
               country_iso,
               type=None,
               pattern=None,
               region=None,
               services=None,
               lata=None,
               rate_center=None,
               limit=None,
               offset=None,
               eligible=None,
               city=None,
               npanxx=None,
               local_calling_area=None):
        return self.client.request('GET', ('PhoneNumber', ),
                                   to_param_dict(self.search, locals()))

    @validate_args(
        services=[
            optional(
                is_iterable(
                    all_of(of_type(six.text_type), is_in(('sms', 'voice', 'mms'))),
                    sep=','))
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
             type=None,
             number_startswith=None,
             subaccount=None,
             alias=None,
             services=None,
             limit=20,
             offset=0):
        return self.client.request(
            'GET',
            ('Number', ),
            to_param_dict(self.list, locals()),
            objects_type=Number,
            response_type=ListResponseObject, )

    @validate_args(number=[is_phonenumber()])
    def get(self, number):
        return self.client.request(
            'GET', ('Number', number), response_type=Number)

    @validate_args(
        numbers=[
            one_of(
                is_iterable(of_type(six.text_type), sep=','),
                of_type(six.text_type))
        ],
        carrier=[of_type(six.text_type)],
        region=[of_type(six.text_type)],
        number_type=[optional(of_type(six.text_type))],
        app_id=[optional(of_type(six.text_type))],
        subaccount=[optional(is_subaccount())])
    def create(self,
               numbers,
               carrier,
               region,
               number_type=None,
               app_id=None,
               subaccount=None):
        return self.client.request('POST', ('Number', ),
                                   to_param_dict(self.create, locals()))

    def update(self,
               number,
               app_id=None,
               subaccount=None,
               alias=None,
               verification_info=None,):
        return self.client.request('POST', ('Number', number),
                                   to_param_dict(self.update, locals()))

    def delete(self, number):
        return self.client.request('DELETE', ('Number', number))
