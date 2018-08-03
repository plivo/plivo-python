# -*- coding: utf-8 -*-
"""
Phlo class
"""
from plivo.resources.nodes import Node, MultiPartyCall, Member
from plivo.base import PlivoResource, PlivoResourceInterface
from plivo.utils.validators import *

class Phlo(PlivoResource):
    _name = 'Phlo'
    _identifier_string = 'phlo_id'

    def node(self, node_type, node_id):
        self.node_id = node_id
        data = {
            'phlo_id': self.phlo_id,
            'node_id': node_id,
            'node_type': node_type
        }
        return Node(self.client, data)

    def multi_party_call(self, node_id):
        self.node_id = node_id
        data = {
            'phlo_id': self.phlo_id,
            'node_id': node_id,
            'node_type': 'multi_party_call'
        }
        return MultiPartyCall(self.client, data)

class Phlos(PlivoResourceInterface):
    _resource_type = Phlo

    def __init__(self, client):
        super(Phlos, self).__init__(client)

    @validate_args(phlo_id=[of_type(six.text_type)])
    def get(self, phlo_id):
        self.phlo_id = phlo_id
        data = {
            'phlo_id': self.phlo_id,
        }
        return Phlo(self.client, data)
