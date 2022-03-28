# -*- coding: utf-8 -*-
"""
Conference class - along with its list class
"""
from plivo.utils.validators import *
from plivo.utils import to_param_dict

from plivo.base import PlivoResource, PlivoResourceInterface
from plivo.exceptions import InvalidRequestError
from plivo.utils import to_param_dict


class ConferenceMember(PlivoResource):
    _name = ''
    _identifier_string = 'member_id'


class Conference(PlivoResource):
    _name = 'Conference'
    _identifier_string = 'conference_name'

    def hangup(self):
        return self.client.conferences.hangup(self.conference_name)

    def member_hangup(self, member_id):
        return self.client.conferences.member_hangup(self.conference_name,
                                                     member_id)

    def member_kick(self, member_id):
        return self.client.conferences.member_kick(self.conference_name,
                                                   member_id)

    def member_mute(self, member_id):
        return self.client.conferences.member_mute(self.conference_name,
                                                   member_id)

    def member_mute_stop(self, member_id):
        return self.client.conferences.member_mute_stop(
            self.conference_name, member_id)

    def member_deaf(self, member_id):
        return self.client.conferences.member_deaf(self.conference_name,
                                                   member_id)

    def member_deaf_stop(self, member_id):
        return self.client.conferences.member_deaf_stop(
            self.conference_name, member_id)

    def member_play(self, member_id, url):
        return self.client.conferences.member_play(self.conference_name,
                                                   member_id, url)

    def member_play_stop(self, member_id):
        return self.client.conferences.member_play_stop(
            self.conference_name, member_id)

    def member_speak(self, member_id, text, voice=None, language=None):
        return self.client.conferences.member_speak(self.conference_name,
                                                    member_id, text,
                                                    **to_param_dict(
                                                        self.member_speak,
                                                        locals()))

    def member_speak_stop(self, member_id):
        return self.client.conferences.member_speak_stop(
            self.conference_name, member_id)

    def record(self,
               file_format=None,
               transcription_type=None,
               transcription_url=None,
               transcription_method=None,
               callback_url=None,
               callback_method=None):
        return self.client.conferences.record(self.conference_name,
                                              **to_param_dict(
                                                  self.member_speak, locals()))

    def record_stop(self):
        return self.client.conferences.record_stop(self.conference_name)


class Conferences(PlivoResourceInterface):
    _resource_type = Conference
    _iterable = False

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def list(self, callback_url=None, callback_method=None):
        return self.client.request('GET', ('Conference', ), to_param_dict(self.list, locals()), is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def get(self, conference_name, callback_url=None, callback_method=None):
        return self.client.request('GET', ('Conference', conference_name), to_param_dict(self.get, locals()),
                                   is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def delete(self, conference_name, callback_url=None, callback_method=None):
        return self.client.request('DELETE', ('Conference', conference_name), to_param_dict(self.delete, locals()),
                                   is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def delete_all(self, callback_url=None, callback_method=None):
        return self.client.request('DELETE', ('Conference', ), to_param_dict(self.delete_all, locals()),
                                   is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def hangup_all(self, callback_url=None, callback_method=None):
        return self.delete_all(callback_url, callback_method)

    def hangup(self, conference_name):
        return self.delete(conference_name)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def member_speak(self,
                     conference_name,
                     member_id,
                     text,
                     voice=None,
                     language=None,
                     callback_url=None,
                     callback_method=None):
        return self.client.request(
            'POST',
            ('Conference', conference_name, 'Member', member_id, 'Speak'),
            to_param_dict(self.member_speak, locals()), is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def member_play(self, conference_name, member_id, url, callback_url=None, callback_method=None):
        return self.client.request(
            'POST',
            ('Conference', conference_name, 'Member', member_id, 'Play'),
            to_param_dict(self.member_play, locals()), is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def member_deaf(self, conference_name, member_id, callback_url=None, callback_method=None):
        return self.client.request(
            'POST',
            ('Conference', conference_name, 'Member', member_id, 'Deaf'),
            to_param_dict(self.member_deaf, locals()), is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def member_mute(self, conference_name, member_id, callback_url=None, callback_method=None):
        return self.client.request(
            'POST',
            ('Conference', conference_name, 'Member', member_id, 'Mute'), to_param_dict(self.member_mute, locals()),
            is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def member_speak_stop(self, conference_name, member_id, callback_url=None, callback_method=None):
        return self.client.request(
            'DELETE',
            ('Conference', conference_name, 'Member', member_id, 'Speak'),
            to_param_dict(self.member_speak_stop, locals()), is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def member_play_stop(self, conference_name, member_id, callback_url=None, callback_method=None):
        return self.client.request(
            'DELETE',
            ('Conference', conference_name, 'Member', member_id, 'Play'),
            to_param_dict(self.member_play_stop, locals()), is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def member_deaf_stop(self, conference_name, member_id, callback_url=None, callback_method=None):
        return self.client.request(
            'DELETE',
            ('Conference', conference_name, 'Member', member_id, 'Deaf'),
            to_param_dict(self.member_deaf_stop, locals()), is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def member_mute_stop(self, conference_name, member_id, callback_url=None, callback_method=None):
        return self.client.request(
            'DELETE',
            ('Conference', conference_name, 'Member', member_id, 'Mute'),
            to_param_dict(self.member_mute_stop, locals()), is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def member_kick(self, conference_name, member_id, callback_url=None, callback_method=None):
        return self.client.request(
            'POST',
            ('Conference', conference_name, 'Member', member_id, 'Kick'),
            to_param_dict(self.member_kick, locals()), is_voice_request=True)

    def member_hangup(self, conference_name, member_id):
        return self.client.request(
            'DELETE', ('Conference', conference_name, 'Member', member_id), is_voice_request=True)

    def record(self,
               conference_name,
               file_format=None,
               transcription_type=None,
               transcription_url=None,
               transcription_method=None,
               callback_url=None,
               callback_method=None):
        return self.client.request('POST',
                                   ('Conference', conference_name, 'Record'),
                                   to_param_dict(self.record, locals()), is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def record_stop(self, conference_name, callback_url=None, callback_method=None):
        return self.client.request('DELETE',
                                   ('Conference', conference_name, 'Record'),
                                   to_param_dict(self.record_stop, locals()), is_voice_request=True)
