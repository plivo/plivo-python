from plivo.utils.validators import *
from plivo.utils.location import *

class Parameter:
    @validate_args(
        type=[required(of_type_exact(str))],
        text=[optional(of_type_exact(str, type(None)))],
        media=[optional(of_type_exact(str))],
        payload=[optional(of_type_exact(str))],
        currency=[optional(of_type_exact(dict))],
        date_time=[optional(of_type_exact(dict))],
        location=[optional(validate_dict_items(Location))]
    )
    def __init__(self, type, text=None, media=None, payload=None, currency=None, date_time=None, location=None):
        self.type = type
        self.text = text
        self.media = media
        self.payload = payload
        self.currency = Currency(**currency) if currency else None
        self.date_time = DateTime(**date_time) if date_time else None
        self.location = location

class Component:
    @validate_args(
        type=[required(of_type_exact(str))],
        sub_type=[optional(of_type_exact(str, type(None)))],
        index=[optional(of_type_exact(str, type(None)))],
        parameters=[optional(validate_list_items(Parameter))],
    )
    def __init__(self, type, sub_type=None, index=None, parameters=None):
        self.type = type
        self.sub_type = sub_type
        self.index = index
        self.parameters = parameters if parameters is not None else []

class Template:
    @validate_args(
        name=[required(of_type_exact(str))],
        language=[required(of_type_exact(str))],
        components=[optional(validate_list_items(Component))],
    )
    def __init__(self, name, language, components=None):
        self.name = name
        self.language = language
        self.components = components if components is not None else []


class Currency:
    @validate_args(
        fallback_value=[required(of_type_exact(str))],
        currency_code=[required(of_type_exact(str))],
        amount_1000=[required(of_type_exact(int))],
    )
    def __init__(self, fallback_value, currency_code, amount_1000):
        self.fallback_value=fallback_value
        self.currency_code = currency_code
        self.amount_1000 = amount_1000


class DateTime:
    @validate_args(
        fallback_value=[required(of_type_exact(str))],
    )
    def __init__(self, fallback_value):
        self.fallback_value = fallback_value
