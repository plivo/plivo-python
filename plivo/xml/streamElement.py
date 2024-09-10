from plivo import exceptions
from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type
import six


class StreamElement(PlivoXMLElement):
    _name = 'Stream'
    _nestable = []

    ALLOWED_AUDIO_TRACKS = ['inbound', 'outbound', 'both']
    ALLOWED_CALLBACK_METHODS = ['GET', 'POST']

    @property
    def bidirectional(self):
        return self.__bidirectional

    @bidirectional.setter
    def bidirectional(self, value):
        if value is not None:
            if not isinstance(value, bool):
                raise exceptions.ValidationError("bidirectional must be a boolean value.")
        self.__bidirectional = value

    @validate_args(
        value=[of_type(bool)]
    )
    def set_bidirectional(self, value):
        self.bidirectional = value
        return self

    @property
    def audioTrack(self):
        return self.__audioTrack

    @audioTrack.setter
    def audioTrack(self, value):
        if value is not None:
            if value not in self.ALLOWED_AUDIO_TRACKS:
                raise exceptions.ValidationError(f"audioTrack must be one of {self.ALLOWED_AUDIO_TRACKS}.")
        self.__audioTrack = value

    @validate_args(
        value=[of_type(str)]
    )
    def set_audioTrack(self, value):
        self.audioTrack = value
        return self

    @property
    def statusCallbackMethod(self):
        return self.__statusCallbackMethod

    @statusCallbackMethod.setter
    def statusCallbackMethod(self, value):
        if value is not None:
            if value not in self.ALLOWED_CALLBACK_METHODS:
                raise exceptions.ValidationError(f"statusCallbackMethod must be one of {self.ALLOWED_CALLBACK_METHODS}.")
        self.__statusCallbackMethod = value

    @validate_args(
        value=[of_type(str)]
    )
    def set_statusCallbackMethod(self, value):
        self.statusCallbackMethod = value
        return self

    @property
    def keepCallAlive(self):
        return self.__keepCallAlive

    @keepCallAlive.setter
    def keepCallAlive(self, value):
        if value is not None:
            if not isinstance(value, bool):
                raise exceptions.ValidationError("keepCallAlive must be a boolean value.")
        self.__keepCallAlive = value

    @validate_args(
        value=[of_type(bool)]
    )
    def set_keepCallAlive(self, value):
        self.keepCallAlive = value
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
            extraHeaders=None,
            keepCallAlive=None
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
        self.keepCallAlive = keepCallAlive

    def to_dict(self):
        d = {
            'bidirectional': self.bidirectional,
            'audioTrack': self.audioTrack,
            'streamTimeout': self.streamTimeout,
            'statusCallbackUrl': self.statusCallbackUrl,
            'statusCallbackMethod': self.statusCallbackMethod,
            'contentType': self.contentType,
            'extraHeaders': self.extraHeaders,
            'keepCallAlive': self.keepCallAlive
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }