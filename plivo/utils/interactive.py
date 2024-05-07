from plivo.utils.validators import validate_args, optional, of_type_exact, validate_list_items, validate_dict_items

class Header:
    @validate_args(
        type=[optional(of_type_exact(str, type(None)))],
        text=[optional(of_type_exact(str, type(None)))],
        media=[optional(of_type_exact(str, type(None)))]
    )
    def __init__(self, type=None, text=None, media=None):
        self.type = type
        self.text = text
        self.media = media

class Body:
    @validate_args(
        text=[optional(of_type_exact(str, type(None)))]
    )
    def __init__(self, text=None):
        self.text = text

class Footer:
    @validate_args(
        text=[optional(of_type_exact(str, type(None)))]
    )
    def __init__(self, text=None):
        self.text = text

class Row:
    @validate_args(
        id=[optional(of_type_exact(str, type(None)))],
        title=[optional(of_type_exact(str, type(None)))],
        description=[optional(of_type_exact(str, type(None)))]
    )
    def __init__(self, id=None, title=None, description=None):
        self.id = id
        self.title = title
        self.description = description

class Section:
    @validate_args(
        title=[optional(of_type_exact(str, type(None)))],
        rows=[optional(validate_list_items(Row))]
    )
    def __init__(self, title=None, rows=None):
        self.title = title
        self.rows = rows if rows is not None else []

class Btn:
    @validate_args(
        id=[optional(of_type_exact(str, type(None)))],
        title=[optional(of_type_exact(str, type(None)))],
        cta_url=[optional(of_type_exact(str, type(None)))]
    )
    def __init__(self, id=None, title=None, cta_url=None):
        self.id = id
        self.title = title
        self.cta_url = cta_url

class Action:
    @validate_args(
        buttons=[optional(validate_list_items(Btn))],
        sections=[optional(validate_list_items(Section))]
    )
    def __init__(self, buttons=None, sections=None):
        self.buttons = buttons if buttons is not None else []
        self.sections = sections if sections is not None else []

class Interactive:
    @validate_args(
        type=[optional(of_type_exact(str, type(None)))],
        header=[optional(validate_dict_items(Header))],
        body=[optional(validate_dict_items(Body))],
        footer=[optional(validate_dict_items(Footer))],
        action=[optional(validate_dict_items(Action))]
    )
    def __init__(self, type=None, header=None, body=None, footer=None, action=None):
        self.type = type
        # Assign directly the validated dictionary or default to None if not provided
        self.header = header
        self.body = body
        self.footer = footer
        self.action = action
