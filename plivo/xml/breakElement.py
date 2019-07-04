from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type


class BreakElement(PlivoXMLElement):
    _name = 'break'
    _nestable = []

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        self.__strength = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_strength(self, value):
        self.strength = value
        return self

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_time(self, value):
        self.time = value
        return self

    def __init__(
        self,
        content=None,
        strength=None,
        time=None,
    ):

        super(BreakElement, self).__init__()
        self.content = content
        self.strength = strength
        self.time = time

    def to_dict(self):
        d = {
            'strength': self.strength,
            'time': self.time,
        }

        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
