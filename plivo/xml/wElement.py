from plivo.utils.validators import *
from plivo.xml import (
    PlivoXMLElement,
    map_type,
    BreakElement,
    EmphasisElement,
    PhonemeElement,
    ProsodyElement,
    SayAsElement,
    SubElement
)


class WElement(PlivoXMLElement):
    _name = 'w'
    _nestable = [
        'break',
        'emphasis',
        'phoneme',
        'prosody',
        'say-as',
        'sub'
    ]

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_role(self, value):
        self.role = value
        return self

    def __init__(
        self,
        content=None,
        role=None,
    ):

        super(WElement, self).__init__()
        self.content = content
        self.role = role

    def to_dict(self):
        d = {
            'role': self.role,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }

    def add_break(
        self,
        strength=None,
        time=None
    ):

        self.add(
            BreakElement(
                strength=strength,
                time=time,
            ))
        return self

    def add_emphasis(
        self,
        content,
        level=None,
    ):

        self.add(
            EmphasisElement(
                content=content,
                level=level,
            ))
        return self

    def add_phoneme(
        self,
        content,
        alphabet=None,
        ph=None,
    ):

        self.add(
            PhonemeElement(
                content=content,
                alphabet=alphabet,
                ph=ph,
            ))
        return self

    def add_prosody(
        self,
        content,
        volume=None,
        rate=None,
        pitch=None,
    ):

        self.add(
            ProsodyElement(
                content=content,
                volume=volume,
                rate=rate,
                pitch=pitch,
            ))
        return self

    def add_say_as(
        self,
        content,
        interpret_as=None,
        format=None,
    ):

        self.add(
            SayAsElement(
                content=content,
                interpret_as=interpret_as,
                format=format,
            ))
        return self

    def add_sub(
        self,
        content,
        alias=None,
    ):

        self.add(
            SubElement(
                content=content,
                alias=alias,
            ))
        return self
