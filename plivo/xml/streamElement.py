from plivo.utils.validators import *
from plivo.xml import (
    PlivoXMLElement,
    map_type,
    BreakElement,
    EmphasisElement,
    LangElement,
)


class StreamElement(PlivoXMLElement):
    _name = 'Stream'
    _nestable = [
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
            bidirectional=None,
            audioTrack=None,
            streamTimeout=None,
            statusCallbackUrl=None,
            statusCallbackMethod=None,
            contentType=None,
            extraHeaders=None
    ):
        super(StreamElement, self).__init__()

        self.content = content
        self.bidirectional = bidirectional
        self.audioTrack = audioTrack
        self.streamTimeout = streamTimeout
        self.statusCallbackUrl = statusCallbackUrl
        self.statusCallbackMethod = statusCallbackMethod
        self.contentType = contentType
        self.extraHeaders = extraHeaders


    def to_dict(self):
        d = {
            'bidirectional': self.bidirectional,
            'audioTrack': self.audioTrack,
            'streamTimeout': self.streamTimeout,
            'statusCallbackUrl': self.statusCallbackUrl,
            'statusCallbackMethod': self.statusCallbackMethod,
            'contentType': self.contentType,
            'extraHeaders': self.extraHeaders,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
