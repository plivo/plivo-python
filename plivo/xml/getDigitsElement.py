from plivo.xml import (
    PlivoXMLElement,
    map_type,
    SpeakElement,
    PlayElement,
    WaitElement
)
from plivo.utils.validators import *


class GetDigitsElement(PlivoXMLElement):
    _name = 'GetDigits'
    _nestable = [
        'Speak',
        'Play',
        'Wait'
    ]

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
    def digit_timeout(self):
        return self.__digit_timeout

    @digit_timeout.setter
    def digit_timeout(self, value):
        self.__digit_timeout = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_digit_timeout(self, value):
        self.digit_timeout = value
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
    def num_digits(self):
        return self.__num_digits

    @num_digits.setter
    def num_digits(self, value):
        self.__num_digits = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_num_digits(self, value):
        self.num_digits = value
        return self

    @property
    def retries(self):
        return self.__retries

    @retries.setter
    def retries(self, value):
        self.__retries = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_retries(self, value):
        self.retries = value
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
    def valid_digits(self):
        return self.__valid_digits

    @valid_digits.setter
    def valid_digits(self, value):
        self.__valid_digits = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_valid_digits(self, value):
        self.valid_digits = value
        return self

    @property
    def invalid_digits_sound(self):
        return self.__invalid_digits_sound

    @invalid_digits_sound.setter
    def invalid_digits_sound(self, value):
        self.__invalid_digits_sound = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_invalid_digits_sound(self, value):
        self.invalid_digits_sound = value
        return self

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self, value):
        self.__log = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_log(self, value):
        self.log = value
        return self

    def __init__(
            self,
            action=None,
            method=None,
            timeout=None,
            digit_timeout=None,
            finish_on_key=None,
            num_digits=None,
            retries=None,
            redirect=None,
            play_beep=None,
            valid_digits=None,
            invalid_digits_sound=None,
            log=None,
    ):
        super(GetDigitsElement, self).__init__()

        self.action = action
        self.method = method
        self.timeout = timeout
        self.digit_timeout = digit_timeout
        self.finish_on_key = finish_on_key
        self.num_digits = num_digits
        self.retries = retries
        self.redirect = redirect
        self.play_beep = play_beep
        self.valid_digits = valid_digits
        self.invalid_digits_sound = invalid_digits_sound
        self.log = log

    def to_dict(self):
        d = {
            'action': self.action,
            'method': self.method,
            'timeout': self.timeout,
            'digitTimeout': self.digit_timeout,
            'finishOnKey': self.finish_on_key,
            'numDigits': self.num_digits,
            'retries': self.retries,
            'redirect': self.redirect,
            'playBeep': self.play_beep,
            'validDigits': self.valid_digits,
            'invalidDigitsSound': self.invalid_digits_sound,
            'log': self.log,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }

    def add_speak(
            self,
            content,
            voice=None,
            language=None,
            loop=None,
    ):
        self.add(
            SpeakElement(
                content=content,
                voice=voice,
                language=language,
                loop=loop,
            ))
        return self

    def add_play(
            self,
            content,
            loop=None,
    ):
        self.add(PlayElement(
            content=content,
            loop=loop,
        ))
        return self

    def add_wait(
            self,
            length=None,
            silence=None,
            min_silence=None,
            beep=None,
    ):

        self.add(
            WaitElement(
                length=length,
                silence=silence,
                min_silence=min_silence,
                beep=beep,
            ))
        return self
