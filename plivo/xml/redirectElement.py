import six

from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type


class RedirectElement(PlivoXMLElement):
    _name = 'Redirect'
    _nestable = []

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

    def __init__(
            self,
            content,
            method=None,
    ):
        super(RedirectElement, self).__init__()

        self.content = content
        self.method = method

    def to_dict(self):
        d = {
            'method': self.method,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
