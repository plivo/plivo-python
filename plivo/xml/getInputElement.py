from plivo.xml import (
    PlivoXMLElement,
    map_type,
    SpeakElement,
    PlayElement,
    WaitElement
)
from plivo.utils.validators import *


class GetInputElement(PlivoXMLElement):
    _name = 'GetInput'
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
    def input_type(self):
        return self.__input_type

    @input_type.setter
    def input_type(self, value):
        self.__input_type = six.text_type(value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_input_type(self, value):
        self.input_type = value
        return self

    @property
    def execution_timeout(self):
        return self.__execution_timeout

    @execution_timeout.setter
    def execution_timeout(self, value):
        self.__execution_timeout = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_execution_timeout(self, value):
        self.execution_timeout = value
        return self

    @property
    def digit_end_timeout(self):
        return self.__digit_end_timeout

    @digit_end_timeout.setter
    def digit_end_timeout(self, value):
        self.__digit_end_timeout = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_digit_end_timeout(self, value):
        self.digit_end_timeout = value
        return self

    @property
    def speech_end_timeout(self):
        return self.__speech_end_timeout

    @speech_end_timeout.setter
    def speech_end_timeout(self, value):
        self.__speech_end_timeout = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_speech_end_timeout(self, value):
        self.speech_end_timeout = value
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
    def speech_model(self):
        return self.__speech_model

    @speech_model.setter
    def speech_model(self, value):
        self.__speech_model = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_speech_model(self, value):
        self.speech_model = value
        return self

    @property
    def hints(self):
        return self.__hints

    @hints.setter
    def hints(self, value):
        self.__hints = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_hints(self, value):
        self.hints = value
        return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_language(self, value):
        self.language = value
        return self

    @property
    def interim_speech_results_callback(self):
        return self.__interim_speech_results_callback

    @interim_speech_results_callback.setter
    def interim_speech_results_callback(self, value):
        self.__interim_speech_results_callback = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_interim_speech_results_callback(self, value):
        self.interim_speech_results_callback = value
        return self

    @property
    def interim_speech_results_callback_method(self):
        return self.__interim_speech_results_callback_method

    @interim_speech_results_callback_method.setter
    def interim_speech_results_callback_method(self, value):
        self.__interim_speech_results_callback_method = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_interim_speech_results_callback_method(self, value):
        self.interim_speech_results_callback_method = value
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
    def profanity_filter(self):
        return self.__profanity_filter

    @profanity_filter.setter
    def profanity_filter(self, value):
        self.__profanity_filter = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_profanity_filter(self, value):
        self.profanity_filter = value
        return self

    def __init__(
            self,
            action=None,
            method=None,
            input_type=None,
            execution_timeout=None,
            digit_end_timeout=None,
            speech_end_timeout=None,
            finish_on_key=None,
            num_digits=None,
            speech_model=None,
            hints=None,
            language=None,
            interim_speech_results_callback=None,
            interim_speech_results_callback_method=None,
            log=None,
            redirect=None,
            profanity_filter=None,
    ):
        super(GetInputElement, self).__init__()

        self.action = action
        self.method = method
        self.input_type = input_type
        self.execution_timeout = execution_timeout
        self.digit_end_timeout = digit_end_timeout
        self.speech_end_timeout = speech_end_timeout
        self.finish_on_key = finish_on_key
        self.num_digits = num_digits
        self.speech_model = speech_model
        self.hints = hints
        self.language = language
        self.interim_speech_results_callback = interim_speech_results_callback
        self.interim_speech_results_callback_method = interim_speech_results_callback_method
        self.log = log
        self.redirect = redirect
        self.profanity_filter = profanity_filter

    def to_dict(self):
        d = {
            'action': self.action,
            'method': self.method,
            'inputType': self.input_type,
            'executionTimeout': self.execution_timeout,
            'digitEndTimeout': self.digit_end_timeout,
            'speechEndTimeout': self.speech_end_timeout,
            'finishOnKey': self.finish_on_key,
            'numDigits': self.num_digits,
            'speechModel': self.speech_model,
            'hints': self.hints,
            'language': self.language,
            'interimSpeechResultsCallback': self.interim_speech_results_callback,
            'interimSpeechResultsCallbackMethod': self.interim_speech_results_callback_method,
            'log': self.log,
            'redirect': self.redirect,
            'profanityFilter': self.profanity_filter
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
