# -*- coding: utf-8 -*-
"""
Phlo class
"""
from plivo.base import PlivoResource, PlivoResourceInterface
from plivo.resources.nodes import Node, MultiPartyCall, Member
from plivo.utils import to_param_dict
from plivo.utils.validators import *


class Phlo(PlivoResource):
    _name = 'Phlo'
    _identifier_string = 'phlo_id'

    def node(self, node_type, node_id):
        self.node_id = node_id
        return self.client.request(
            'GET', ('phlo', self.phlo_id, node_type, node_id), response_type=Node)

    def multi_party_call(self, node_id):
        self.node_id = node_id
        self.node_type = 'multi_party_call'
        return self.client.request(
            'GET', ('phlo', self.phlo_id, self.node_type, node_id), response_type=MultiPartyCall)

    def run(self, **kwargs):
        return self.client.request('POST', ('account', self.client.session.auth[0], 'phlo', self.phlo_id),
                                   to_param_dict(self.run, kwargs, func_args_check=False))

    @validate_args(
        phlo_id=[of_type(six.text_type)],
        node_id=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
    )
    def member(self, phlo_id, node_id,
               member_id, action,
               node_type='conference_bridge'):
        """
        :param phlo_id:
        :param node_id:
        :param member_id:
        :param action:
        :param node_type: default value `conference_bridge`
        :return:
        """
        return self.client.phlo.member(phlo_id, node_id,
                                       member_id, action,
                                       node_type
                                       )


class Phlos(PlivoResourceInterface):
    _resource_type = Phlo

    def __init__(self, client):
        super(Phlos, self).__init__(client)

    @validate_args(phlo_id=[of_type(six.text_type)])
    def get(self, phlo_id):
        self.phlo_id = phlo_id
        return self.client.request(
            'GET', ('phlo', phlo_id), response_type=Phlo)

    @validate_args(
        phlo_id=[of_type(six.text_type)],
        node_id=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
    )
    def member(self, phlo_id, node_id,
               member_id, action,
               node_type='conference_bridge'):
        """
        :param phlo_id:
        :param node_id:
        :param member_id:
        :param action:
        :param node_type: default value `conference_bridge`
        :return:
        """
        data = {
            'member_id': member_id,
            'phlo_id': phlo_id,
            'node_id': node_id,
            'node_type': node_type
        }
        member = Member(self.client, data)
        return getattr(member, action)()

    @validate_args(
        phlo_id=[of_type(six.text_type)],
        node_id=[of_type(six.text_type)],
        action=[of_type(six.text_type)],
        member_id=[optional(of_type(six.text_type))]
    )
    def multi_party_call(self, phlo_id, node_id, action,
                        member_id=None, trigger_source=None,
                        to=None, role=None):
        data = {
            'phlo_id': phlo_id,
            'node_id': node_id,
            'node_type': 'multi_party_call',
        }

        multi_party_call = MultiPartyCall(self.client, data)

        if action == 'member':
            if not member_id:
                raise ValidationError(
                    'member_id parameter is required'
                )
            return getattr(multi_party_call, action)(member_id)

        if not trigger_source:
            raise ValidationError(
                'trigger_source parameter is required'
            )

        if not to:
            raise ValidationError(
                'to parameter is required'
            )

        if action == 'call' and not role:
            raise ValidationError(
                'role parameter is required'
            )

        return getattr(multi_party_call, action)(trigger_source, to, role)
