from plivo.utils.validators import *
from plivo.xml import (
    PlivoXMLElement,
    map_type
)


class StreamElement(PlivoXMLElement):
    _name = 'Stream'
    _nestable = [
    ]

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