from plivo.xml import PlivoXMLElement, map_type
from plivo.utils.validators import *


class HangupElement(PlivoXMLElement):
    _name = 'Hangup'
    _nestable = []

    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = six.text_type(value) if value is not None else None

    @validate_args(
        value=[of_type(six.text_type)],
    )
    def set_reason(self, value):
        self.reason = value
        return self

    @property
    def schedule(self):
        return self.__schedule

    @schedule.setter
    def schedule(self, value):
        self.__schedule = int(value) if value is not None else None

    @validate_args(
        value=[of_type(*six.integer_types)],
    )
    def set_schedule(self, value):
        self.schedule = value
        return self

    def __init__(
            self,
            reason=None,
            schedule=None,
    ):
        super(HangupElement, self).__init__()

        self.reason = reason
        self.schedule = schedule

    def to_dict(self):
        d = {
            'reason': self.reason,
            'schedule': self.schedule,
        }
        return {
            k: six.text_type(map_type(v))
            for k, v in d.items() if v is not None
        }
