from plivo.utils.validators import *
from plivo.xml import (
    PlivoXMLElement,
    map_type,
    BreakElement,
    EmphasisElement,
    LangElement,
)


class SpeakElement(PlivoXMLElement):
    _name = 'Speak'
    _nestable = [
        'break',
        'cont',
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
    def voice(self):
        return self.__voice

    @voice.setter
    def voice(self, value):
        self.__voice = six.text_type(value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_voice(self, value):
        self.voice = value
        return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = six.text_type(value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_language(self, value):
        self.language = value
        return self

    @property
    def loop(self):
        return self.__loop

    @loop.setter
    def loop(self, value):
        self.__loop = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_loop(self, value):
        self.loop = value
        return self

    def __init__(
            self,
            content,
            voice=None,
            language=None,
            loop=None,
    ):
        super(SpeakElement, self).__init__()

        self.content = content
        self.voice = voice
        self.language = language
        self.loop = loop

    def to_dict(self):
        d = {
            'voice': self.voice,
            'language': self.language,
            'loop': self.loop,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }

    def add_break(
        self,
        content=None,
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

    def add_cont(
        self,
        content
    ):
        from .contElement import ContElement
        self.add(
            ContElement(
                content=content,
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
