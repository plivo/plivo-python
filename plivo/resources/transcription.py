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

    def get_transcription(self):
        return self.client.transcriptions.get_transcription(self.id, **to_param_dict(self.get_transcription(), locals()))

    def create_transcription(self):
        return self.client.transcriptions.create_transcription(self.id, **to_param_dict(self.create_transcription(), locals()))

    def delete_transcription(self):
        return self.client.transcriptions.delete_transcription(self.id, **to_param_dict(self.delete_transcription(), locals()))


class Transcriptions(PlivoResourceInterface):
    _resource_type = Transcription

    @validate_args(transcription_id=[of_type(six.text_type)]
                   )
    def get_transcription(self, transcription_id, type=None):
        if not type:
            return self.client.request(
                'GET', ('Transcription', transcription_id), is_voice_request=True)
        else:
            return self.client.request(
                'GET', ('Transcription', transcription_id), to_param_dict(self.get_transcription, locals()), is_voice_request=True)

    def create_transcription(self, recording_id, transcription_callback_url=None):
        return self.client.request(
            'POST', ('Transcription', recording_id), to_param_dict(self.create_transcription, locals()), is_voice_request=True)

    def delete_transcription(self, transcription_id):
        return self.client.request(
            'DELETE', ('Transcription', transcription_id), is_voice_request=True)



