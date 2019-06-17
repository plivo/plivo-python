import six

from plivo.xml import (
    PlivoXMLElement,
    map_type,
    BreakElement,
    EmphasisElement,
    LangElement,
    PhonemeElement,
    ProsodyElement,
)


class SElement(PlivoXMLElement):
    _name = 's'
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

    def __init__(
        self,
        content=None,
    ):

        super(SElement, self).__init__()
        self.content = content

    def to_dict(self):
        d = {}
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
