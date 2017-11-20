import six

from plivo.xml import PlivoXMLElement, map_type


class SpeakElement(PlivoXMLElement):
    _name = 'Speak'
    _nestable = []

    @property
    def voice(self):
        return self.__voice

    @voice.setter
    def voice(self, value):
        self.__voice = six.text_type(value) if value is not None else None

    def set_voice(self, value):
        self.voice = value
        return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = six.text_type(value) if value is not None else None

    def set_language(self, value):
        self.language = value
        return self

    @property
    def loop(self):
        return self.__loop

    @loop.setter
    def loop(self, value):
        self.__loop = int(value) if value is not None else None

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
