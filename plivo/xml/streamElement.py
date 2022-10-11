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
        self.extraHeaders = self.process_extra_headers(extraHeaders)

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

    def process_extra_headers(self, extraHeaders):
        if not extraHeaders: return

        if not type(extraHeaders) is dict: raise TypeError('extraHeaders needs to be passed in as a dictionary object!')

        res = {}
        for key in extraHeaders:
            if not key.endswith('X-PH'):
                new_key = key + 'X-PH'
                res[new_key] = extraHeaders[key]
            else:
                res[key] = extraHeaders[key]

        return res
