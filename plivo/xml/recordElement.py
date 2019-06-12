from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type


class RecordElement(PlivoXMLElement):
    _name = 'Record'
    _nestable = []

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
    def file_format(self):
        return self.__file_format

    @file_format.setter
    def file_format(self, value):
        self.__file_format = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_file_format(self, value):
        self.file_format = value
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
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, value):
        self.__timeout = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_timeout(self, value):
        self.timeout = value
        return self

    @property
    def max_length(self):
        return self.__max_length

    @max_length.setter
    def max_length(self, value):
        self.__max_length = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_max_length(self, value):
        self.max_length = value
        return self

    @property
    def play_beep(self):
        return self.__play_beep

    @play_beep.setter
    def play_beep(self, value):
        self.__play_beep = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_play_beep(self, value):
        self.play_beep = value
        return self

    @property
    def finish_on_key(self):
        return self.__finish_on_key

    @finish_on_key.setter
    def finish_on_key(self, value):
        self.__finish_on_key = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_finish_on_key(self, value):
        self.finish_on_key = value
        return self

    @property
    def record_session(self):
        return self.__record_session

    @record_session.setter
    def record_session(self, value):
        self.__record_session = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_record_session(self, value):
        self.record_session = value
        return self

    @property
    def start_on_dial_answer(self):
        return self.__start_on_dial_answer

    @start_on_dial_answer.setter
    def start_on_dial_answer(self, value):
        self.__start_on_dial_answer = bool(
            value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_start_on_dial_answer(self, value):
        self.start_on_dial_answer = value
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

    def __init__(
            self,
            action=None,
            method=None,
            file_format=None,
            redirect=None,
            timeout=None,
            max_length=None,
            play_beep=None,
            finish_on_key=None,
            record_session=None,
            start_on_dial_answer=None,
            transcription_type=None,
            transcription_url=None,
            transcription_method=None,
            callback_url=None,
            callback_method=None,
    ):
        super(RecordElement, self).__init__()

        self.action = action
        self.method = method
        self.file_format = file_format
        self.redirect = redirect
        self.timeout = timeout
        self.max_length = max_length
        self.play_beep = play_beep
        self.finish_on_key = finish_on_key
        self.record_session = record_session
        self.start_on_dial_answer = start_on_dial_answer
        self.transcription_type = transcription_type
        self.transcription_url = transcription_url
        self.transcription_method = transcription_method
        self.callback_url = callback_url
        self.callback_method = callback_method

    def to_dict(self):
        d = {
            'action': self.action,
            'method': self.method,
            'fileFormat': self.file_format,
            'redirect': self.redirect,
            'timeout': self.timeout,
            'maxLength': self.max_length,
            'playBeep': self.play_beep,
            'finishOnKey': self.finish_on_key,
            'recordSession': self.record_session,
            'startOnDialAnswer': self.start_on_dial_answer,
            'transcriptionType': self.transcription_type,
            'transcriptionUrl': self.transcription_url,
            'transcriptionMethod': self.transcription_method,
            'callbackUrl': self.callback_url,
            'callbackMethod': self.callback_method,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
