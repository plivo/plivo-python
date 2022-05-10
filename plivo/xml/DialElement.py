from plivo.utils.validators import *
from plivo.xml import (
    PlivoXMLElement,
    map_type,
    NumberElement,
    UserElement
)


class DialElement(PlivoXMLElement):
    _name = 'Dial'
    _nestable = ['User', 'Number']

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
    def caller_id(self):
        return self.__caller_id

    @caller_id.setter
    def caller_id(self, value):
        self.__caller_id = six.text_type(value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_caller_id(self, value):
        self.caller_id = value
        return self

    @property
    def caller_name(self):
        return self.__caller_name

    @caller_name.setter
    def caller_name(self, value):
        self.__caller_name = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_caller_name(self, value):
        self.caller_name = value
        return self

    @property
    def confirm_sound(self):
        return self.__confirm_sound

    @confirm_sound.setter
    def confirm_sound(self, value):
        self.__confirm_sound = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_confirm_sound(self, value):
        self.confirm_sound = value
        return self

    @property
    def confirm_timeout(self):
        return self.confirm_timeout

    @confirm_timeout.setter
    def confirm_timeout(self, value):
        self.confirm_timeout = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def confirm_timeout(self, value):
        self.confirm_timeout = value
        return self

    @property
    def confirm_key(self):
        return self.__confirm_key

    @confirm_key.setter
    def confirm_key(self, value):
        self.__confirm_key = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_confirm_key(self, value):
        self.confirm_key = value
        return self

    @property
    def dial_music(self):
        return self.__dial_music

    @dial_music.setter
    def dial_music(self, value):
        self.__dial_music = six.text_type(value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_dial_music(self, value):
        self.dial_music = value
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
    def digits_match_b_leg(self):
        return self.__digits_match_b_leg

    @digits_match_b_leg.setter
    def digits_match_b_leg(self, value):
        self.__digits_match_b_leg = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_digits_match_b_leg(self, value):
        self.digits_match_b_leg = value
        return self

    @property
    def sip_headers(self):
        return self.__sip_headers

    @sip_headers.setter
    def sip_headers(self, value):
        self.__sip_headers = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_sip_headers(self, value):
        self.sip_headers = value
        return self

    def __init__(
            self,
            action=None,
            method=None,
            hangup_on_star=None,
            time_limit=None,
            timeout=None,
            caller_id=None,
            caller_name=None,
            confirm_sound=None,
            confirm_timeout=None,
            confirm_key=None,
            dial_music=None,
            callback_url=None,
            callback_method=None,
            redirect=None,
            digits_match=None,
            digits_match_b_leg=None,
            sip_headers=None,
    ):
        super(DialElement, self).__init__()

        self.action = action
        self.method = method
        self.hangup_on_star = hangup_on_star
        self.time_limit = time_limit
        self.timeout = timeout
        self.caller_id = caller_id
        self.caller_name = caller_name
        self.confirm_sound = confirm_sound
        self.confirm_timeout = confirm_timeout
        self.confirm_key = confirm_key
        self.dial_music = dial_music
        self.callback_url = callback_url
        self.callback_method = callback_method
        self.redirect = redirect
        self.digits_match = digits_match
        self.digits_match_b_leg = digits_match_b_leg
        self.sip_headers = sip_headers

    def to_dict(self):
        d = {
            'action': self.action,
            'method': self.method,
            'hangupOnStar': self.hangup_on_star,
            'timeLimit': self.time_limit,
            'timeout': self.timeout,
            'callerId': self.caller_id,
            'callerName': self.caller_name,
            'confirmSound': self.confirm_sound,
            'confirmTimeout': self.confirm_timeout,
            'confirmKey': self.confirm_key,
            'dialMusic': self.dial_music,
            'callbackUrl': self.callback_url,
            'callbackMethod': self.callback_method,
            'redirect': self.redirect,
            'digitsMatch': self.digits_match,
            'digitsMatchBLeg': self.digits_match_b_leg,
            'sipHeaders': self.sip_headers,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
            }

    def add_user(
            self,
            content,
            send_digits=None,
            send_on_preanswer=None,
            sip_headers=None,
    ):
        self.add(
            UserElement(
                content=content,
                send_digits=send_digits,
                send_on_preanswer=send_on_preanswer,
                sip_headers=sip_headers,
            ))
        return self

    def add_number(
            self,
            content,
            send_digits=None,
            send_on_preanswer=None,
    ):
        self.add(
            NumberElement(
                content=content,
                send_digits=send_digits,
                send_on_preanswer=send_on_preanswer,
            ))
        return self
