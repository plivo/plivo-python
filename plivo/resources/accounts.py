# -*- coding: utf-8 -*-
"""
Account & Subaccount classes - along with their list classes
"""

from plivo.base import (ListResponseObject,
                        PlivoResource,
                        PlivoResourceInterface)
from plivo.utils import to_param_dict
from plivo.utils.validators import *


class Subaccount(PlivoResource):
    _name = 'Subaccount'
    _identifier_string = 'auth_id'

    def update(self, name, enabled=False):
        return self.client.subaccounts.update(self.id, name, enabled)

    def delete(self, cascade=None):
        return self.client.subaccounts.delete(self.id, cascade)


class Subaccounts(PlivoResourceInterface):
    _resource_type = Subaccount

    @validate_args(auth_id=[is_subaccount_id()])
    def get(self, auth_id):
        return self.client.request(
            'GET', ('Subaccount', auth_id), response_type=Subaccount)

    @validate_args(
        name=[of_type(six.text_type)], enabled=[of_type_exact(bool)])
    def create(self, name, enabled=False):
        return self.client.request(
            'POST', ('Subaccount', ),
            to_param_dict(self.create, locals()),
            response_type=Subaccount)

    @validate_args(
        auth_id=[is_subaccount_id()],
        name=[of_type(six.text_type)],
        enabled=[optional(of_type_exact(bool))])
    def update(self, auth_id, name, enabled=False):
        return self.client.request('POST', ('Subaccount', auth_id),
                                   to_param_dict(self.update, locals()))

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
            'GET', ('Subaccount', ),
            to_param_dict(self.list, locals()),
            response_type=ListResponseObject,
            objects_type=Subaccount)

    @validate_args(
        auth_id=[is_subaccount_id()],
        cascade=[
            optional(of_type_exact(bool))
        ])
    def delete(self, auth_id, cascade=None):
        return self.client.request(
            'DELETE', ('Subaccount', auth_id),
            to_param_dict(self.delete, locals())
        )


class Account(PlivoResource):
    _name = 'Account'
    _identifier_string = 'auth_id'

    def get(self):
        return self.client.account.get()

    def update(self, name=None, city=None, address=None):
        id = self.id
        self.__dict__.update(to_param_dict(self.update, locals()))
        return self.client.account.update(*to_param_dict(
            self.update, locals()))


class Accounts(PlivoResourceInterface):
    _resource_type = Account

    def get(self):
        return self.client.request('GET', tuple(), response_type=Account)

    @validate_args(
        name=[optional(of_type(six.text_type))],
        city=[optional(of_type(six.text_type))],
        address=[optional(of_type(six.text_type))])
    def update(self, name=None, city=None, address=None):
        if not (name or city or address):
            raise ValidationError(
                'One parameter of name, city and address is required')
        return self.client.request(
            'POST', tuple(), {'name': name,
                              'city': city,
                              'address': address})
