import six

from plivo.xml import (
    PlayElement,
    PlivoXMLElement,
    SpeakElement,
    WaitElement,
    map_type,
    DTMFElement,
    GetDigitsElement,
    RedirectElement,
    MessageElement,
)


class PreAnswerElement(PlivoXMLElement):
    _name = 'PreAnswer'
    _nestable = [
        'Speak',
        'Play',
        'Wait',
        'GetDigits',
        'Redirect',
        'Message',
        'DTMF'
    ]

    def __init__(self):
        super(PreAnswerElement, self).__init__()

    def to_dict(self):
        d = {}
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }

    def add_speak(
            self,
            content,
            voice=None,
            language=None,
            loop=None, ):
        self.add(
            SpeakElement(
                content=content,
                voice=voice,
                language=language,
                loop=loop, ))
        return self

    def add_play(
            self,
            content,
            loop=None, ):
        self.add(PlayElement(
            content=content,
            loop=loop, ))
        return self

    def add_wait(
            self,
            length=None,
            silence=None,
            min_silence=None,
            beep=None, ):
        self.add(
            WaitElement(
                length=length,
                silence=silence,
                min_silence=min_silence,
                beep=beep, ))
        return self

    def add_get_digits(
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
        self.add(
            GetDigitsElement(
                action=action,
                method=method,
                timeout=timeout,
                digit_timeout=digit_timeout,
                finish_on_key=finish_on_key,
                num_digits=num_digits,
                retries=retries,
                redirect=redirect,
                play_beep=play_beep,
                valid_digits=valid_digits,
                invalid_digits_sound=invalid_digits_sound,
                log=log,
            ))
        return self

    def add_redirect(
            self,
            content,
            method=None,
    ):
        self.add(
            RedirectElement(
                content=content,
                method=method,
            ))
        return self

    def add_message(
            self,
            content,
            src=None,
            dst=None,
            type=None,
            callback_url=None,
            callback_method=None,
    ):
        self.add(
            MessageElement(
                content=content,
                src=src,
                dst=dst,
                type=type,
                callback_url=callback_url,
                callback_method=callback_method,
            ))
        return self

    def add_dtmf(
            self,
            content,
            async_=None,
    ):
        self.add(
            DTMFElement(
                content=content,
                async_=async_,
            ))
        return self
