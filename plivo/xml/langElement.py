import six

from plivo.xml import (
    PlivoXMLElement,
    map_type,
    BreakElement,
)


class LangElement(PlivoXMLElement):
    _name = 'Lang'
    _nestable = [
        "Break",
        "Emphasis",
        "Lang",
        "P",
        "Phoneme",
        "Prosody",
        "S",
        "SayAs",
        "Sub",
        "W"
    ]

    @property
    def xmllang(self):
        return self.__xmllang

    @xmllang.setter
    def xmllang(self, value):
        self.__xmllang = six.text_type(
            value) if value is not None else None

    def set_xmllang(self, value):
        self.xmllang = value
        return self

    def __init__(
        self,
        content=None,
        xmllang=None,
    ):

        super(LangElement, self).__init__()
        self.content = content
        self.xmllang = xmllang

    def to_dict(self):
        d = {
            'xmllang': self.xmllang,
        }

        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }

    def add_break(
        self,
        content,
        strength=None,
        time=None
    ):
        self.add(
            BreakElement(
                content=content,
                strength=strength,
                time=time,
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

    def add_p(
        self,
        content,
    ):
        from .pElement import PElement

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
