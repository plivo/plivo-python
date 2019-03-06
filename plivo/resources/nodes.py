# -*- coding: utf-8 -*-
"""
Node class
"""
from plivo.base import PlivoResource
from plivo.utils import to_param_dict
from plivo.utils.validators import *


class Node(PlivoResource):
    _name = 'Node'
    _identifier_string = 'node_id'

    @validate_args(
        action=[of_type(six.text_type)])
    def update(self,
               action,
               trigger_source,
               to,
               role):
        return self.client.request('POST', ('phlo', self.phlo_id, self.node_type, self.node_id),
                                   to_param_dict(self.update, locals()))


class MultiPartyCall(Node):
    _name = 'MultiPartyCall'
    _identifier_string = 'node_id'

    def call(self,
             trigger_source,
             to,
             role):
        return self.update('call', trigger_source, to, role)

    def warm_transfer(self,
             trigger_source,
             to,
             role='agent'):
        return self.update('warm_transfer', trigger_source, to, role)

    def cold_transfer(self,
             trigger_source,
             to,
             role='agent'):
        return self.update('cold_transfer', trigger_source, to, role)

    def member(self, member_id):
        self.member_id = member_id
        data = {
            'member_id': member_id,
            'phlo_id': self.phlo_id,
            'node_id': self.node_id,
            'node_type': self.node_type
        }
        return Member(self.client, data)


class Member(PlivoResource):
    _name = 'Member'
    _identifier_string = 'member_id'

    def abort_transfer(self):
        return self.update('abort_transfer')

    def resume_call(self):
        return self.update('resume_call')

    def voicemail_drop(self):
        return self.update('voicemail_drop')

    def hangup(self):
        return self.update('hangup')

    def hold(self):
        return self.update('hold')

    def unhold(self):
        return self.update('unhold')

    def mute(self):
        return self.update('mute')

    def unmute(self):
        return self.update('unmute')

    def update(self,
               action):
        return self.client.request('POST', ('phlo', self.phlo_id, self.node_type, self.node_id, 'members', self.member_id),
                                   to_param_dict(self.update, locals()))
