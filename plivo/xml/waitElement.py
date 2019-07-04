from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type


class WaitElement(PlivoXMLElement):
    _name = 'Wait'
    _nestable = []

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_length(self, value):
        self.length = value
        return self

    @property
    def silence(self):
        return self.__silence

    @silence.setter
    def silence(self, value):
        self.__silence = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_silence(self, value):
        self.silence = value
        return self

    @property
    def min_silence(self):
        return self.__min_silence

    @min_silence.setter
    def min_silence(self, value):
        self.__min_silence = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_min_silence(self, value):
        self.min_silence = value
        return self

    @property
    def beep(self):
        return self.__beep

    @beep.setter
    def beep(self, value):
        self.__beep = bool(value) if value is not None else None

    @validate_args(
        value=[of_type_exact(bool)],
    )
    def set_beep(self, value):
        self.beep = value
        return self

    def __init__(
            self,
            length=None,
            silence=None,
            min_silence=None,
            beep=None,
    ):
        super(WaitElement, self).__init__()

        self.length = length
        self.silence = silence
        self.min_silence = min_silence
        self.beep = beep

    def to_dict(self):
        d = {
            'length': self.length,
            'silence': self.silence,
            'minSilence': self.min_silence,
            'beep': self.beep,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
