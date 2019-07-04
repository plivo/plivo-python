from plivo.utils.validators import *
from plivo.xml import PlivoXMLElement, map_type


class SubElement(PlivoXMLElement):
    _name = 'sub'
    _nestable = []

    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, value):
        self.__alias = six.text_type(
            value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_alias(self, value):
        self.alias = value
        return self

    def __init__(
        self,
        content=None,
        alias=None,
    ):
        super(SubElement, self).__init__()

        self.content = content
        self.alias = alias

    def to_dict(self):
        d = {
            'alias': self.alias,
        }

        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
