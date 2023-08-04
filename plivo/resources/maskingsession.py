from plivo.base import (ListResponseObject, PlivoResource,
                        PlivoResourceInterface)
from plivo.utils import to_param_dict
from plivo.utils.validators import *

class MaskingSession(PlivoResource):
    _name = 'MaskingSession'
    _identifier_string = 'session_uuid'
    def create_masking_session(self):
        return self.client.calls.create_masking_session(self.id,
                                                        **to_param_dict(self.create_masking_session(), locals()))

    def delete_masking_session(self):
        return self.client.calls.delete_masking_session(self.id,
                                                        **to_param_dict(self.delete_masking_session(), locals()))

    def get_masking_session(self):
        return self.client.calls.get_masking_session(self.id,
                                                     **to_param_dict(self.get_masking_session(), locals()))

    def update_masking_session(self):
        return self.client.calls.update_masking_session(self.id,
                                                        **to_param_dict(self.update_masking_session(), locals()))

    def list_masking_session(self):
        return self.client.calls.list_masking_session(self.id,
                                                      **to_param_dict(self.list_masking_session(), locals()))


class MaskingSessions(PlivoResourceInterface):
    _resource_type = MaskingSession

    @validate_args(
        callback_url=[optional(is_url())],
        recording_callback_url=[optional(is_url())],
        first_party_play_url=[optional(is_url())],
        second_party_play_url=[optional(is_url())],
    )
    def create_masking_session(self,
                               first_party=None,
                               second_party=None,
                               session_expiry=None,
                               call_time_limit=None,
                               record=None,
                               record_file_format=None,
                               recording_callback_url=None,
                               initiate_call_to_first_party=None,
                               callback_url=None,
                               callback_method=None,
                               ring_timeout=None,
                               first_party_play_url=None,
                               second_party_play_url=None,
                               recording_callback_method=None
                               ):
        return self.client.request('POST', ('Masking', 'Session',),
                                   to_param_dict(self.create_masking_session, locals()), is_voice_request=True)

    def delete_masking_session(self,
                               session_uuid
                               ):
        return self.client.request('DELETE', ('Masking', 'Session', session_uuid),
                                   to_param_dict(self.delete_masking_session, locals()), is_voice_request=True)

    def get_masking_session(self,
                            session_uuid
                            ):
        return self.client.request('GET', ('Masking', 'Session', session_uuid), is_voice_request=True)

    def update_masking_session(self,
                               session_uuid,
                               session_expiry=None,
                               call_time_limit=None,
                               record=None,
                               record_file_format=None,
                               recording_callback_url=None,
                               callback_url=None,
                               callback_method=None,
                               ring_timeout=None,
                               first_party_play_url=None,
                               second_party_play_url=None,
                               recording_callback_method=None
                               ):
        return self.client.request('POST', ('Masking', 'Session', session_uuid),
                                   to_param_dict(self.update_masking_session, locals()), is_voice_request=True)

    def list_masking_session(self,
                             first_party=None,
                             second_party=None,
                             virtual_number=None,
                             status=None,
                             created_time=None,
                             created_time__lt=None,
                             created_time__lte=None,
                             created_time__gt=None,
                             created_time__gte=None,
                             expiry_time=None,
                             expiry_time__lt=None,
                             expiry_time__lte=None,
                             expiry_time__gt=None,
                             expiry_time__gte=None,
                             duration=None,
                             duration__lt=None,
                             duration__lte=None,
                             duration__gt=None,
                             duration__gte=None,
                             limit=None,
                             offset=None
                             ):
        return self.client.request('GET', ('Masking', 'Session'), to_param_dict(self.list_masking_session, locals()),
                                   is_voice_request=True)
