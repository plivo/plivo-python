from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type


class UserElement(PlivoXMLElement):
    _name = 'User'
    _nestable = []

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
    def send_on_preanswer(self):
        return self.__send_on_preanswer

    @send_on_preanswer.setter
    def send_on_preanswer(self, value):
        self.__send_on_preanswer = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_send_on_preanswer(self, value):
        self.send_on_preanswer = value
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
            content,
            send_digits=None,
            send_on_preanswer=None,
            sip_headers=None,
    ):
        super(UserElement, self).__init__()

        self.content = content
        self.send_digits = send_digits
        self.send_on_preanswer = send_on_preanswer
        self.sip_headers = sip_headers

    def to_dict(self):
        d = {
            'sendDigits': self.send_digits,
            'sendOnPreanswer': self.send_on_preanswer,
            'sipHeaders': self.sip_headers,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
