from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type


class PhonemeElement(PlivoXMLElement):
    _name = 'phoneme'
    _nestable = []

    @property
    def alphabet(self):
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, value):
        self.__alphabet = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_alphabet(self, value):
        self.alphabet = value
        return self

    @property
    def ph(self):
        return self.__ph

    @ph.setter
    def ph(self, value):
        self.__ph = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_ph(self, value):
        self.ph = value
        return self

    def __init__(
        self,
        content=None,
        alphabet=None,
        ph=None,
    ):

        super(PhonemeElement, self).__init__()
        self.content = content
        self.alphabet = alphabet
        self.ph = ph

    def to_dict(self):
        d = {
            'alphabet': self.alphabet,
            'ph': self.ph,
        }

        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
