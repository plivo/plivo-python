from plivo.utils.validators import *

class Parameter:
    @validate_args(
        type=[required(of_type_exact(str))],
        text=[optional(of_type_exact(str, type(None)))],
        media=[optional(of_type_exact(str))],
        currency=[optional(of_type_exact('plivo.utils.template.Currency'))],
        date_time=[optional(of_type_exact('plivo.utils.template.DateTime'))],
    )
    def __init__(self, type, text=None, media=None, currency=None, date_time=None):
        self.type = type
        self.text = text
        self.media = media
        self.currency = currency
        self.date_time = date_time

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
        namespace=[optional(of_type_exact(str))],
        name=[required(of_type_exact(str))],
        language=[required(of_type_exact(str))],
        components=[optional(validate_list_items(Component))],
    )
    def __init__(self, name, language,namespace=None, components=None):
        self.namespace = namespace
        self.name = name
        self.language = language
        self.components = components if components is not None else []


class Currency:
    @validate_args(
        currency_code=[required(of_type_exact(str))],
        amount1000=[required(of_type_exact(int))],
    )
    def __init__(self, currency_code, amount1000):
        self.currency_code = currency_code
        self.amount1000 = amount1000


class DateTime:
    @validate_args(
        component=[required(of_type_exact('plivo.utils.template.HSMDateTimeComponent'))],
    )
    def __init__(self, component):
        self.component = component


class HSMDateTimeComponent:
    @validate_args(
        day_of_week=[optional(of_type_exact(str))],
        year=[optional(of_type_exact(int))],
        month=[optional(of_type_exact(int))],
        day_of_month=[optional(of_type_exact(int))],
        hour=[optional(of_type_exact(int))],
        minute=[optional(of_type_exact(int))],
        calendar=[optional(of_type_exact(str))],
    )
    def __init__(self, day_of_week=None, year=None, month=None, day_of_month=None, hour=None, minute=None, calendar=None):
        self.day_of_week = day_of_week
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.hour = hour
        self.minute = minute
        self.calendar = calendar