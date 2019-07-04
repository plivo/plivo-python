from plivo.utils.validators import *
from plivo.xml import (
    PlivoXMLElement,
    map_type,
    BreakElement,
    EmphasisElement,
    LangElement,
    PElement,
    PhonemeElement,
)


class ProsodyElement(PlivoXMLElement):
    _name = 'prosody'
    _nestable = [
        'break',
        'emphasis',
        'lang',
        'p',
        'phoneme',
        'prosody',
        's',
        'say-as',
        'sub',
        'w'
    ]

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_volume(self, value):
        self.volume = value
        return self

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, value):
        self.__rate = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_rate(self, value):
        self.rate = value
        return self

    @property
    def pitch(self):
        return self.__pitch

    @pitch.setter
    def pitch(self, value):
        self.__pitch = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_pitch(self, value):
        self.pitch = value
        return self

    def __init__(
        self,
        content=None,
        volume=None,
        rate=None,
        pitch=None
    ):
        super(ProsodyElement, self).__init__()
        self.content = content
        self.volume = volume
        self.rate = rate
        self.pitch = pitch

    def to_dict(self):
        d = {
            'volume': self.volume,
            'rate': self.rate,
            'pitch': self.pitch,
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

    def add_lang(
        self,
        content,
        xmllang=None,
    ):
        self.add(
            LangElement(
                content=content,
                xmllang=xmllang,
            ))
        return self

    def add_p(
        self,
        content,
    ):
        self.add(
            PElement(
                content=content,
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

    def add_s(
        self,
        content,
    ):
        from .sElement import SElement
        self.add(
            SElement(
                content=content,
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
