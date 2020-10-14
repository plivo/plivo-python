# -*- coding: utf-8 -*-
"""
Application class - along with its list class
"""

from plivo.base import (ListResponseObject, PlivoResource, PlivoResourceInterface, SecondaryPlivoResource)
from plivo.utils.validators import *
from plivo.utils import to_param_dict


class MultiPartyCall(PlivoResource):
    _name = 'MultiPartyCall'
    _identifier_string = 'mpc_uuid'

    def add_participant(self,
                        role,
                        from_=None,
                        to_=None,
                        call_uuid=None,
                        call_status_callback_url=None,
                        call_status_callback_method='POST',
                        sip_headers=None,
                        confirm_key=None,
                        confirm_key_sound_url=None,
                        confirm_key_sound_method='GET',
                        dial_music='Real',
                        ring_timeout=45,
                        max_duration=14400,
                        max_participants=10,
                        wait_music_url=None,
                        wait_music_method='GET',
                        agent_hold_music_url=None,
                        agent_hold_music_method='GET',
                        customer_hold_music_url=None,
                        customer_hold_music_method='GET',
                        recording_callback_url=None,
                        recording_callback_method='GET',
                        status_callback_url=None,
                        status_callback_method='GET',
                        on_exit_action_url=None,
                        on_exit_action_method='POST',
                        record=False,
                        record_file_format='mp3',
                        status_callback_events='mpc-state-changes,participant-state-changes',
                        stay_alone=False,
                        coach_mode=True,
                        mute=False,
                        hold=False,
                        start_mpc_on_enter=True,
                        end_mpc_on_exit=False,
                        relay_dtmf_inputs=False,
                        enter_sound='beep:1',
                        enter_sound_method='GET',
                        exit_sound='beep:2',
                        exit_sound_method='GET'
                        ):
        return self.client.multi_party_calls.add_participant(role, uuid=self.id,
                                                             **to_param_dict(self.add_participant, locals()))

    def start(self):
        return self.client.multi_party_calls.start(uuid=self.id)

    def stop(self):
        return self.client.multi_party_calls.stop(uuid=self.id)

    def start_recording(self, file_format=None, status_callback_url=None, status_callback_method=None):
        return self.client.multi_party_calls.start_recording(uuid=self.id,
                                                             **to_param_dict(self.add_participant, locals()))

    def stop_recording(self):
        return self.client.multi_party_calls.stop_recording(uuid=self.id)

    def pause_recording(self):
        return self.client.multi_party_calls.pause_recording(uuid=self.id)

    def resume_recording(self):
        return self.client.multi_party_calls.resume_recording(uuid=self.id)

    def get(self):
        return self.client.multi_party_calls.get(uuid=self.id)

    def update(self, participant_id, coach_mode=None, hold=None, mute=None):
        return self.client.multi_party_calls.update_participant(participant_id=participant_id,
                                                                uuid=self.id,
                                                                coach_mode=coach_mode,
                                                                mute=mute,
                                                                hold=hold)

    def kick(self, participant_id):
        return self.client.multi_party_calls.kick_participant(participant_id=participant_id, uuid=self.id)

    def get_participant(self, participant_id):
        return self.client.multi_party_calls.get_participant(participant_id=participant_id, uuid=self.id)


class MultiPartyCallParticipant(SecondaryPlivoResource):
    _name = 'MultiPartyCall'
    _identifier_string = 'mpc_uuid'
    _secondary_identifier_string = 'member_id'

    def update(self, coach_mode=None, hold=None, mute=None):
        return self.client.multi_party_calls.update_participant(participant_id=self.secondary_id,
                                                                uuid=self.id,
                                                                coach_mode=coach_mode,
                                                                mute=mute,
                                                                hold=hold)

    def kick(self):
        return self.client.multi_party_calls.kick_participant(participant_id=self.secondary_id, uuid=self.id)

    def get(self):
        return self.client.multi_party_calls.get_participant(participant_id=self.secondary_id, uuid=self.id)


class MultiPartyCalls(PlivoResourceInterface):
    _resource_type = MultiPartyCall

    @staticmethod
    def __make_mpc_id(friendly_name=None, uuid=None):
        if not uuid and not friendly_name:
            raise ValidationError('specify either multi party call friendly name or uuid')
        if uuid and friendly_name:
            raise ValidationError('cannot specify both multi party call friendly name or uuid')
        return 'uuid_' + str(uuid) if uuid else 'name_' + str(friendly_name)

    @staticmethod
    def __clean_identifiers(params):
        params.pop('friendly_name', None)
        params.pop('uuid', None)
        params.pop('participant_id', None)
        return params

    @validate_args(
        sub_account=[optional(is_subaccount())],
        friendly_name=[optional(of_type_exact(str))],
        status=[optional(of_type_exact(str),
                         is_in(('active', 'initialized', 'ended'), case_sensitive=False, case_type='lower'))],
        termination_cause_code=[optional(of_type_exact(int))],
        end_time__gt=[optional(is_proper_date_format())],
        end_time__gte=[optional(is_proper_date_format())],
        end_time__lt=[optional(is_proper_date_format())],
        end_time__lte=[optional(is_proper_date_format())],
        creation_time__gt=[optional(is_proper_date_format())],
        creation_time__gte=[optional(is_proper_date_format())],
        creation_time__lt=[optional(is_proper_date_format())],
        creation_time__lte=[optional(is_proper_date_format())],
        limit=[optional(of_type(int), check(lambda limit: 0 < limit <= 20, '0 < limit <= 20'))],
        offset=[optional(of_type(int), check(lambda offset: 0 <= offset, '0 <= offset'))]
    )
    def list(self,
             sub_account=None,
             friendly_name=None,
             status=None,
             termination_cause_code=None,
             end_time__gt=None,
             end_time__gte=None,
             end_time__lt=None,
             end_time__lte=None,
             creation_time__gt=None,
             creation_time__gte=None,
             creation_time__lt=None,
             creation_time__lte=None,
             limit=None,
             offset=None
             ):
        return self.client.request('GET', ('MultiPartyCall',), to_param_dict(self.list, locals()),
                                   response_type=ListResponseObject, objects_type=MultiPartyCall, is_voice_request=True)

    @validate_args(
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
    )
    def get(self, uuid=None, friendly_name=None):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        return self.client.request('GET', ('MultiPartyCall', mpc_id),
                                   is_voice_request=True, response_type=MultiPartyCall)

    @validate_args(
        role=[of_type_exact(str), is_in(('agent', 'supervisor', 'customer'), case_sensitive=False, case_type='lower')],
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
        from_=[optional(is_phonenumber())],
        to_=[optional(is_iterable(of_type_exact(str), sep='<'))],
        call_uuid=[optional(of_type_exact(str))],
        call_status_callback_url=[optional(of_type_exact(str), is_url())],
        call_status_callback_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))],
        confirm_key=[
            optional(of_type_exact(str), is_in(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#', '*'),
                                               case_sensitive=False))],
        confirm_key_sound_url=[optional(of_type_exact(str), is_url())],
        confirm_key_sound_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))],
        dial_music=[optional(
            of_type_exact(str),
            one_of(is_url(), is_in(('real', 'none'), case_sensitive=False, case_type='lower')),
        )],
        ring_timeout=[optional(
            of_type_exact(int),
            check(lambda ring_timeout: 15 <= ring_timeout <= 120, '15 < ring_timeout <= 120')
        )],
        max_duration=[optional(
            of_type_exact(int),
            check(lambda max_duration: 300 <= max_duration <= 28800, '300 < max_duration <= 28800'))],
        max_participants=[optional(
            of_type_exact(int),
            check(lambda max_participants: 2 <= max_participants <= 10, '2 < max_participants <= 10')
        )],
        wait_music_url=[optional(of_type_exact(str), is_url())],
        wait_music_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))],
        agent_hold_music_url=[optional(of_type_exact(str), is_url())],
        agent_hold_music_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))],
        customer_hold_music_url=[optional(of_type_exact(str), is_url())],
        customer_hold_music_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))],
        recording_callback_url=[optional(of_type_exact(str), is_url())],
        recording_callback_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))],
        status_callback_url=[optional(of_type_exact(str), is_url())],
        status_callback_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))],
        on_exit_action_url=[optional(of_type_exact(str), is_url())],
        on_exit_action_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))],
        record=[optional(of_type_exact(bool))],
        record_file_format=[optional(of_type_exact(str), is_in(('mp3', 'wav'), case_sensitive=False,
                                                               case_type='lower'))],
        status_callback_events=[optional(of_type_exact(str), multi_is_in(('mpc-state-changes',
                                                                          'participant-state-changes',
                                                                          'participant-speak-events',
                                                                          'participant-digit-input-events',
                                                                          'add-participant-api-events'),
                                                                         case_sensitive=False,
                                                                         make_lower_case=True))],
        stay_alone=[optional(of_type_exact(bool))],
        coach_mode=[optional(of_type_exact(bool))],
        mute=[optional(of_type_exact(bool))],
        hold=[optional(of_type_exact(bool))],
        start_mpc_on_enter=[optional(of_type_exact(bool))],
        end_mpc_on_exit=[optional(of_type_exact(bool))],
        relay_dtmf_inputs=[optional(of_type_exact(bool))],
        enter_sound=[optional(
            of_type_exact(str),
            one_of(is_url(), is_in(('beep:1', 'beep:2', 'none'), case_sensitive=False, case_type='lower'))
        )],
        enter_sound_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))],
        exit_sound=[optional(
            of_type_exact(str),
            one_of(is_url(), is_in(('beep:1', 'beep:2', 'none'), case_sensitive=False, case_type='lower')),
        )],
        exit_sound_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))]
    )
    def add_participant(self,
                        role,
                        friendly_name=None,
                        uuid=None,
                        from_=None,
                        to_=None,
                        call_uuid=None,
                        call_status_callback_url=None,
                        call_status_callback_method='POST',
                        sip_headers=None,
                        confirm_key=None,
                        confirm_key_sound_url=None,
                        confirm_key_sound_method='GET',
                        dial_music='Real',
                        ring_timeout=45,
                        max_duration=14400,
                        max_participants=10,
                        wait_music_url=None,
                        wait_music_method='GET',
                        agent_hold_music_url=None,
                        agent_hold_music_method='GET',
                        customer_hold_music_url=None,
                        customer_hold_music_method='GET',
                        recording_callback_url=None,
                        recording_callback_method='GET',
                        status_callback_url=None,
                        status_callback_method='GET',
                        on_exit_action_url=None,
                        on_exit_action_method='POST',
                        record=False,
                        record_file_format='mp3',
                        status_callback_events='mpc-state-changes,participant-state-changes',
                        stay_alone=False,
                        coach_mode=True,
                        mute=False,
                        hold=False,
                        start_mpc_on_enter=True,
                        end_mpc_on_exit=False,
                        relay_dtmf_inputs=False,
                        enter_sound='beep:1',
                        enter_sound_method='GET',
                        exit_sound='beep:2',
                        exit_sound_method='GET'
                        ):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        if (from_ or to_) and call_uuid:
            raise ValidationError('cannot specify call_uuid when (from, to) is provided')
        if not from_ and not to_ and not call_uuid:
            raise ValidationError('specify either call_uuid or (from, to)')
        if call_uuid is None and (not from_ or not to_):
            raise ValidationError('specify (from, to) when not adding an existing call_uuid to multi party participant')
        return self.client.request('POST', ('MultiPartyCall', mpc_id, 'Participant'),
                                   self.__clean_identifiers(to_param_dict(self.add_participant, locals())),
                                   is_voice_request=True)

    @validate_args(
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
    )
    def start(self, uuid=None, friendly_name=None):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        return self.client.request('POST', ('MultiPartyCall', mpc_id), {'status': 'active'})

    @validate_args(
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
    )
    def stop(self, uuid=None, friendly_name=None):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        return self.client.request('DELETE', ('MultiPartyCall', mpc_id), is_voice_request=True)

    @validate_args(
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
        file_format=[optional(of_type_exact(str), is_in(('mp3', 'wav'), case_sensitive=False,
                                                        case_type='lower'))],
        status_callback_url=[optional(of_type_exact(str), is_url())],
        status_callback_method=[optional(of_type_exact(str), is_in(('GET', 'POST'), case_sensitive=False))],
    )
    def start_recording(self,
                        uuid=None,
                        friendly_name=None,
                        file_format='mp3',
                        status_callback_url=None,
                        status_callback_method='POST'):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        return self.client.request('POST', ('MultiPartyCall', mpc_id, 'Record'),
                                   self.__clean_identifiers(to_param_dict(self.start_recording, locals())),
                                   is_voice_request=True)

    @validate_args(
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
    )
    def stop_recording(self, uuid=None, friendly_name=None):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        return self.client.request('DELETE', ('MultiPartyCall', mpc_id, 'Record'), is_voice_request=True)

    @validate_args(
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
    )
    def pause_recording(self, uuid=None, friendly_name=None):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        return self.client.request('POST', ('MultiPartyCall', mpc_id, 'Record', 'Pause'), is_voice_request=True)

    @validate_args(
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
    )
    def resume_recording(self, uuid=None, friendly_name=None):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        return self.client.request('POST', ('MultiPartyCall', mpc_id, 'Record', 'Resume'), is_voice_request=True)

    @validate_args(
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
        call_uuid=[optional(of_type_exact(str))]
    )
    def list_participants(self, uuid=None, friendly_name=None, call_uuid=None):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        return self.client.request('GET', ('MultiPartyCall', mpc_id, 'Participant'),
                                   self.__clean_identifiers(to_param_dict(self.list_participants, locals())),
                                   response_type=ListResponseObject, objects_type=MultiPartyCallParticipant,
                                   is_voice_request=True)

    @validate_args(
        participant_id=[one_of(of_type_exact(str), of_type_exact(int))],
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
        coach_mode=[optional(of_type_exact(bool))],
        mute=[optional(of_type_exact(bool))],
        hold=[optional(of_type_exact(bool))]
    )
    def update_participant(self, participant_id, uuid=None, friendly_name=None, coach_mode=None, mute=None, hold=None):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        if str(participant_id).lower() == 'all' and coach_mode is not None:
            raise ValidationError('cannot specify coach_mode when updating all participants')
        if all(u is None for u in [coach_mode, mute, hold]):
            raise ValidationError('update at least one of coach_mode, mute or hold')
        return self.client.request('POST', ('MultiPartyCall', mpc_id, 'Participant', participant_id),
                                   self.__clean_identifiers(to_param_dict(self.update_participant, locals())),
                                   is_voice_request=True)

    @validate_args(
        participant_id=[one_of(of_type_exact(str), of_type_exact(int))],
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
    )
    def kick_participant(self, participant_id, uuid=None, friendly_name=None):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        return self.client.request('DELETE', ('MultiPartyCall', mpc_id, 'Participant', participant_id),
                                   is_voice_request=True)

    @validate_args(
        participant_id=[one_of(of_type_exact(str), of_type_exact(int))],
        friendly_name=[optional(of_type_exact(str))],
        uuid=[optional(of_type_exact(str))],
    )
    def get_participant(self, participant_id, uuid=None, friendly_name=None):
        mpc_id = self.__make_mpc_id(friendly_name, uuid)
        return self.client.request('GET', ('MultiPartyCall', mpc_id, 'Participant', participant_id),
                                   response_type=MultiPartyCallParticipant, is_voice_request=True)
