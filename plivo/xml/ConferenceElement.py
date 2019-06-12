from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type


class ConferenceElement(PlivoXMLElement):
    _name = 'Conference'
    _nestable = []

    @property
    def muted(self):
        return self.__muted

    @muted.setter
    def muted(self, value):
        self.__muted = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_muted(self, value):
        self.muted = value
        return self

    @property
    def enter_sound(self):
        return self.__enter_sound

    @enter_sound.setter
    def enter_sound(self, value):
        self.__enter_sound = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_enter_sound(self, value):
        self.enter_sound = value
        return self

    @property
    def exit_sound(self):
        return self.__exit_sound

    @exit_sound.setter
    def exit_sound(self, value):
        self.__exit_sound = six.text_type(value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_exit_sound(self, value):
        self.exit_sound = value
        return self

    @property
    def start_conference_on_enter(self):
        return self.__start_conference_on_enter

    @start_conference_on_enter.setter
    def start_conference_on_enter(self, value):
        self.__start_conference_on_enter = bool(
            value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_start_conference_on_enter(self, value):
        self.start_conference_on_enter = value
        return self

    @property
    def end_conference_on_exit(self):
        return self.__end_conference_on_exit

    @end_conference_on_exit.setter
    def end_conference_on_exit(self, value):
        self.__end_conference_on_exit = bool(
            value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_end_conference_on_exit(self, value):
        self.end_conference_on_exit = value
        return self

    @property
    def stay_alone(self):
        return self.__stay_alone

    @stay_alone.setter
    def stay_alone(self, value):
        self.__stay_alone = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_stay_alone(self, value):
        self.stay_alone = value
        return self

    @property
    def wait_sound(self):
        return self.__wait_sound

    @wait_sound.setter
    def wait_sound(self, value):
        self.__wait_sound = six.text_type(value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_wait_sound(self, value):
        self.wait_sound = value
        return self

    @property
    def max_members(self):
        return self.__max_members

    @max_members.setter
    def max_members(self, value):
        self.__max_members = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_max_members(self, value):
        self.max_members = value
        return self

    @property
    def record(self):
        return self.__record

    @record.setter
    def record(self, value):
        self.__record = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_record(self, value):
        self.record = value
        return self

    @property
    def record_file_format(self):
        return self.__record_file_format

    @record_file_format.setter
    def record_file_format(self, value):
        self.__record_file_format = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_record_file_format(self, value):
        self.record_file_format = value
        return self

    @property
    def time_limit(self):
        return self.__time_limit

    @time_limit.setter
    def time_limit(self, value):
        self.__time_limit = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_time_limit(self, value):
        self.time_limit = value
        return self

    @property
    def hangup_on_star(self):
        return self.__hangup_on_star

    @hangup_on_star.setter
    def hangup_on_star(self, value):
        self.__hangup_on_star = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_hangup_on_star(self, value):
        self.hangup_on_star = value
        return self

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, value):
        self.__action = six.text_type(value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_action(self, value):
        self.action = value
        return self

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = six.text_type(value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_method(self, value):
        self.method = value
        return self

    @property
    def callback_url(self):
        return self.__callback_url

    @callback_url.setter
    def callback_url(self, value):
        self.__callback_url = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_callback_url(self, value):
        self.callback_url = value
        return self

    @property
    def callback_method(self):
        return self.__callback_method

    @callback_method.setter
    def callback_method(self, value):
        self.__callback_method = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_callback_method(self, value):
        self.callback_method = value
        return self

    @property
    def digits_match(self):
        return self.__digits_match

    @digits_match.setter
    def digits_match(self, value):
        self.__digits_match = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_digits_match(self, value):
        self.digits_match = value
        return self

    @property
    def floor_event(self):
        return self.__floor_event

    @floor_event.setter
    def floor_event(self, value):
        self.__floor_event = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_floor_event(self, value):
        self.floor_event = value
        return self

    @property
    def redirect(self):
        return self.__redirect

    @redirect.setter
    def redirect(self, value):
        self.__redirect = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_redirect(self, value):
        self.redirect = value
        return self

    @property
    def relay_dtmf(self):
        return self.__relay_dtmf

    @relay_dtmf.setter
    def relay_dtmf(self, value):
        self.__relay_dtmf = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_relay_dtmf(self, value):
        self.relay_dtmf = value
        return self

    @property
    def send_digits(self):
        return self.__send_digits

    @send_digits.setter
    def send_digits(self, value):
        self.__send_digits = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_send_digits(self, value):
        self.send_digits = value
        return self

    @property
    def record_when_alone(self):
        return self.__record_when_alone

    @record_when_alone.setter
    def record_when_alone(self, value):
        self.__record_when_alone = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_record_when_alone(self, value):
        self.record_when_alone = value
        return self

    @property
    def transcription_type(self):
        return self.__transcription_type

    @transcription_type.setter
    def transcription_type(self, value):
        self.__transcription_type = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_transcription_type(self, value):
        self.transcription_type = value
        return self

    @property
    def transcription_url(self):
        return self.__transcription_url

    @transcription_url.setter
    def transcription_url(self, value):
        self.__transcription_url = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_transcription_url(self, value):
        self.transcription_url = value
        return self

    @property
    def transcription_method(self):
        return self.__transcription_method

    @transcription_method.setter
    def transcription_method(self, value):
        self.__transcription_method = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_transcription_method(self, value):
        self.transcription_method = value
        return self

    def __init__(
            self,
            content=None,
            muted=None,
            enter_sound=None,
            exit_sound=None,
            start_conference_on_enter=None,
            end_conference_on_exit=None,
            stay_alone=None,
            wait_sound=None,
            max_members=None,
            record=None,
            record_file_format=None,
            time_limit=None,
            hangup_on_star=None,
            action=None,
            method=None,
            callback_url=None,
            callback_method=None,
            digits_match=None,
            floor_event=None,
            redirect=None,
            relay_dtmf=None,
            send_digits=None,
            record_when_alone=None,
            transcription_type=None,
            transcription_url=None,
            transcription_method=None,
    ):
        super(ConferenceElement, self).__init__()

        self.content = content
        self.muted = muted
        self.enter_sound = enter_sound
        self.exit_sound = exit_sound
        self.start_conference_on_enter = start_conference_on_enter
        self.end_conference_on_exit = end_conference_on_exit
        self.stay_alone = stay_alone
        self.wait_sound = wait_sound
        self.max_members = max_members
        self.record = record
        self.record_file_format = record_file_format
        self.time_limit = time_limit
        self.hangup_on_star = hangup_on_star
        self.action = action
        self.method = method
        self.callback_url = callback_url
        self.callback_method = callback_method
        self.digits_match = digits_match
        self.floor_event = floor_event
        self.redirect = redirect
        self.relay_dtmf = relay_dtmf
        self.send_digits = send_digits
        self.record_when_alone = record_when_alone
        self.transcription_type = transcription_type
        self.transcription_url = transcription_url
        self.transcription_method = transcription_method

    def to_dict(self):
        d = {
            'muted': self.muted,
            'enterSound': self.enter_sound,
            'exitSound': self.exit_sound,
            'startConferenceOnEnter': self.start_conference_on_enter,
            'endConferenceOnExit': self.end_conference_on_exit,
            'stayAlone': self.stay_alone,
            'waitSound': self.wait_sound,
            'maxMembers': self.max_members,
            'record': self.record,
            'recordFileFormat': self.record_file_format,
            'timeLimit': self.time_limit,
            'hangupOnStar': self.hangup_on_star,
            'action': self.action,
            'method': self.method,
            'callbackUrl': self.callback_url,
            'callbackMethod': self.callback_method,
            'digitsMatch': self.digits_match,
            'floorEvent': self.floor_event,
            'redirect': self.redirect,
            'relayDTMF': self.relay_dtmf,
            'sendDigits': self.send_digits,
            'recordWhenAlone': self.record_when_alone,
            'transcriptionType': self.transcription_type,
            'transcriptionUrl': self.transcription_url,
            'transcriptionMethod': self.transcription_method,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
