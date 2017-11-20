import six

from plivo.xml import PlivoXMLElement, map_type


class DTMFElement(PlivoXMLElement):
    _name = 'DTMF'
    _nestable = []

    @property
    def async(self):
        return self.__async

    @async.setter
    def async(self, value):
        self.__async = bool(value) if value is not None else None

    def set_async(self, value):
        self.async = value
        return self

    def __init__(
            self,
            content,
            async=None,
    ):
        super(DTMFElement, self).__init__()

        self.content = content
        self.async = async

    def to_dict(self):
        d = {
            'async': self.async,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
