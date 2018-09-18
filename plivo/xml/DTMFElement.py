import six

from plivo.xml import PlivoXMLElement, map_type


class DTMFElement(PlivoXMLElement):
    _name = 'DTMF'
    _nestable = []

    @property
    def async_(self):
        return self.__async

    @async_.setter
    def async_(self, value):
        self.__async = bool(value) if value is not None else None

    def set_async(self, value):
        self.async_ = value
        return self

    def __init__(
            self,
            content,
            async_=None,
    ):
        super(DTMFElement, self).__init__()

        self.content = content
        self.async_ = async_

    def to_dict(self):
        d = {
            'async': self.async_,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
