# -*- coding: utf-8 -*-
"""
Recording class - along with its list class
"""

from plivo.base import (ListResponseObject, PlivoResource,
                        PlivoResourceInterface)
from plivo.resources.accounts import Subaccount
from plivo.utils import is_valid_time_comparison, to_param_dict
from plivo.utils.validators import *


class Transcription(PlivoResource):
    _name = 'Transcription'
    _identifier_string = 'transcription_id'

    def get_tanscription(self):
        return self.client.transcriptions.get_tanscription(self.id, **to_param_dict(self.get_tanscription(), locals()))

    def create_tanscription(self):
        return self.client.transcriptions.create_tanscription(self.id, **to_param_dict(self.create_tanscription(), locals()))

    def delete_tanscription(self):
        return self.client.transcriptions.delete_tanscription(self.id, **to_param_dict(self.delete_tanscription(), locals()))


class Transcriptions(PlivoResourceInterface):
    _resource_type = Transcription

    @validate_args(transcription_id=[of_type(six.text_type)]
                   )
    def get_tanscription(self, transcription_id, type=None):
        return self.client.request(
                'GET', ('Transcription', transcription_id), to_param_dict(self.get_tanscription, locals()), is_voice_request=True)

    def create_tanscription(self, recording_id, transcription_callback_url=None):
        return self.client.request(
            'POST', ('Transcription', recording_id), to_param_dict(self.create_tanscription, locals()), is_voice_request=True)

    def delete_tanscription(self, transcription_id):
        return self.client.request(
            'DELETE', ('Transcription', transcription_id), is_voice_request=True)



