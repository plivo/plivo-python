from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type


class SayAsElement(PlivoXMLElement):
    _name = 'say-as'
    _nestable = []

    @property
    def interpret_as(self):
        return self.__interpret_as

    @interpret_as.setter
    def interpret_as(self, value):
        self.__interpret_as = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_interpret_as(self, value):
        self.interpret_as = value
        return self

    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, value):
        self.__format = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_format(self, value):
        self.format = value
        return self

    def __init__(
        self,
        content,
        interpret_as=None,
        format=None,
    ):

        super(SayAsElement, self).__init__()
        self.content = content
        self.interpret_as = interpret_as
        self.format = format

    def to_dict(self):
        d = {
            'interpret-as': self.interpret_as,
            'format': self.format,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
