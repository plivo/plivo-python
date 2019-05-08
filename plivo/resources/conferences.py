# -*- coding: utf-8 -*-
"""
Conference class - along with its list class
"""
from plivo.base import PlivoResource, PlivoResourceInterface
from plivo.utils import to_param_dict
from plivo.utils.validators import *


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
            self.conference_name, member_id
        )

    def member_speak(self,
                     member_id,
                     text,
                     voice="WOMAN",     #Changed the value to "WOMAN" since the default value is WOMAN
                     language=None):
        return self.client.conferences.member_speak(
            self.conference_name, member_id, text, **to_param_dict( self.member_speak, locals())
        )

    def member_speak_stop(self, member_id):
        return self.client.conferences.member_speak_stop(
            self.conference_name, member_id
        )

    def record(self,
               file_format=None,
               transcription_type=None,
               transcription_url=None,
               transcription_method=None,
               callback_url=None,
               callback_method=None):
        return self.client.conferences.record(
            self.conference_name, **to_param_dict(self.member_speak, locals())
        )

    def record_stop(self):
        return self.client.conferences.record_stop(self.conference_name)


class Conferences(PlivoResourceInterface):
    _resource_type = Conference
    _iterable = False

    def list(self):
        return self.client.request('GET', ('Conference', ))

    @validate_args(
        conference_name=[of_type(six.text_type)]
    )
    def get(self, conference_name):
        return self.client.request(
            'GET', ('Conference', conference_name)
        )

    @validate_args(
        conference_name=[of_type(six.text_type)]
    )
    def delete(self, conference_name):
        return self.client.request(
            'DELETE', ('Conference', conference_name)
        )

    def delete_all(self):
        return self.client.request(
            'DELETE', ('Conference', )
        )

    def hangup_all(self):
        return self.delete_all()

    @validate_args(
        conference_name=[of_type(six.text_type)]
    )
    def hangup(self, conference_name):
        return self.delete(conference_name)

    @validate_args(
        conference_name=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
        text=[of_type(six.text_type)],
        voice=[optional(of_type(six.text_type))],
        language=[optional(of_type(six.text_type))],
    )
    def member_speak(self,
                     conference_name,
                     member_id,
                     text,
                     voice="WOMAN",              #Changed the value to "WOMAN" since the default value is WOMAN
                     language=None
                     ):
        return self.client.request(
            'POST', ('Conference', conference_name, 'Member', member_id, 'Speak'),
            to_param_dict(self.member_speak, locals())
        )

    @validate_args(
        conference_name=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
        url=[is_url()],
    )
    def member_play(self, conference_name, member_id, url):
        return self.client.request(
            'POST', ('Conference', conference_name, 'Member', member_id, 'Play'),
            to_param_dict(self.member_play, locals())
        )

    @validate_args(
        conference_name=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
    )
    def member_deaf(self, conference_name, member_id):
        return self.client.request(
            'POST', ('Conference', conference_name, 'Member', member_id, 'Deaf')
        )

    @validate_args(
        conference_name=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
    )
    def member_mute(self, conference_name, member_id):
        return self.client.request(
            'POST', ('Conference', conference_name, 'Member', member_id, 'Mute')
        )

    @validate_args(
        conference_name=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
    )
    def member_speak_stop(self, conference_name, member_id):
        return self.client.request(
            'DELETE', ('Conference', conference_name, 'Member', member_id, 'Speak')
        )

    @validate_args(
        conference_name=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
    )
    def member_play_stop(self, conference_name, member_id):
        return self.client.request(
            'DELETE', ('Conference', conference_name, 'Member', member_id, 'Play')
        )

    @validate_args(
        conference_name=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
    )
    def member_deaf_stop(self, conference_name, member_id):
        return self.client.request(
            'DELETE', ('Conference', conference_name, 'Member', member_id, 'Deaf')
        )

    @validate_args(
        conference_name=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
    )
    def member_mute_stop(self, conference_name, member_id):
        return self.client.request(
            'DELETE', ('Conference', conference_name, 'Member', member_id, 'Mute')
        )

    @validate_args(
        conference_name=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
    )
    def member_kick(self, conference_name, member_id):
        return self.client.request(
            'POST', ('Conference', conference_name, 'Member', member_id, 'Kick')
        )

    @validate_args(
        conference_name=[of_type(six.text_type)],
        member_id=[of_type(six.text_type)],
    )
    def member_hangup(self, conference_name, member_id):
        return self.client.request(
            'DELETE', ('Conference', conference_name, 'Member', member_id)
        )

    @validate_args(
        conference_name=[of_type(six.text_type)],
        file_format=[optional(of_type(six.text_type))],
        transcription_type=[
            optional(of_type(six.text_type), is_in(('auto', 'hybrid')))
        ],
        transcription_url=[optional(is_url())],          #Changed the validation to 'is_url'
        transcription_method=[optional(of_type(six.text_type))],
        callback_url=[optional(is_url())],               #Changed the validation to 'is_url'
        callback_method=[optional(of_type(six.text_type))]
    )
    def record(self,
               conference_name,
               file_format=None,
               transcription_type=None,
               transcription_url=None,
               transcription_method="POST",       #Changed the value to "POST" since the default value is POST
               callback_url=None,
               callback_method="POST"             #Changed the value to "POST" since the default value is POST
               ):
        return self.client.request(
            'POST', ('Conference', conference_name, 'Record')
        )

    def record_stop(self, conference_name):
        return self.client.request(
            'DELETE', ('Conference', conference_name, 'Record')
        )
