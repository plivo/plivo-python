from plivo.xml import (
    PlivoXMLElement,
    map_type,
    BreakElement,
)
from plivo.utils.validators import *


class EmphasisElement(PlivoXMLElement):
    _name = 'emphasis'
    _nestable = [
        'break',
        'emphasis',
        'lang',
        'phoneme',
        'prosody',
        'say-as',
        'sub',
        'w'
    ]

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_level(self, value):
        self.level = value
        return self

    def __init__(
        self,
        content=None,
        level=None,
    ):

        super(EmphasisElement, self).__init__()
        self.content = content
        self.level = level

    def to_dict(self):
        d = {
            'level': self.level,
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

    def add_lang(
        self,
        content,
        xmllang=None,
    ):
        from .langElement import LangElement

        self.add(
            LangElement(
                content=content,
                xmllang=xmllang,
            ))
        return self

    def add_emphasis(
        self,
        content,
        level=None,
    ):
        from .emphasisElement import EmphasisElement

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
        from .phonemeElement import PhonemeElement

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
        from .prosodyElement import ProsodyElement

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
        from .sayAsElement import SayAsElement

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
        from .subElement import SubElement

        self.add(
            SubElement(
                content=content,
                alias=alias,
            ))
        return self

    def add_w(
        self,
        content,
        role=None,
    ):
        from .wElement import WElement

        self.add(
            WElement(
                content=content,
                role=role,
            ))
        return self
