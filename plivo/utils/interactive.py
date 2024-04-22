from plivo.utils.validators import validate_args, optional, of_type_exact, validate_list_items
from plivo.utils.template import Parameter

class WAMedia:
    @validate_args(
        id=[optional(of_type_exact(str, type(None)))],
        link=[optional(of_type_exact(str, type(None)))],
        caption=[optional(of_type_exact(str, type(None)))],
        filename=[optional(of_type_exact(str, type(None)))],
    )
    def __init__(self, id=None, link=None, caption=None, filename=None):
        self.id = id
        self.link = link
        self.caption = caption
        self.filename = filename


class Header:
    @validate_args(
        type=[optional(of_type_exact(str, type(None)))],
        text=[optional(of_type_exact(str, type(None)))],
        image=[optional(of_type_exact(WAMedia, type(None)))],
        document=[optional(of_type_exact(WAMedia, type(None)))],
        video=[optional(of_type_exact(WAMedia, type(None)))]
    )
    def __init__(self, type=None, text=None, image=None, document=None, video=None):
        self.type = type
        self.text = text
        self.image = image
        self.document = document
        self.video = video


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


class Reply:
    @validate_args(
        id=[optional(of_type_exact(str, type(None)))],
        title=[optional(of_type_exact(str, type(None)))]
    )
    def __init__(self, id=None, title=None):
        self.id = id
        self.title = title


class Btn:
    @validate_args(
        type=[optional(of_type_exact(str, type(None)))],
        reply=[optional(of_type_exact(Reply, type(None)))]
    )
    def __init__(self, type=None, reply=None):
        self.type = type
        self.reply = reply


class Product:
    @validate_args(
        product_retailer_id=[optional(of_type_exact(str, type(None)))]
    )
    def __init__(self, product_retailer_id=None):
        self.product_retailer_id = product_retailer_id


class Row:
    @validate_args(
        id=[optional(of_type_exact(str, type(None)))],
        title=[optional(of_type_exact(str, type(None)))],
        description=[optional(of_type_exact(str, type(None)))],
    )
    def __init__(self, id=None, title=None, description=None):
        self.id = id
        self.title = title
        self.description = description

class Section:
    @validate_args(
        title=[optional(of_type_exact(str, type(None)))],
        rows=[optional(validate_list_items(Row))],
        product_items=[optional(validate_list_items(Product))]
    )
    def __init__(self, title=None, rows=None, product_items=None):
        self.title = title
        self.rows = rows if rows is not None else []
        self.product_items = product_items if product_items is not None else []
        
class Action:
    @validate_args(
        button=[optional(of_type_exact(str, type(None)))],
        buttons=[optional(validate_list_items(Btn))],
        product_retailer_id=[optional(of_type_exact(str, type(None)))],
        catalog_id=[optional(of_type_exact(str, type(None)))],
        sections=[optional(validate_list_items(Section))],
        name=[optional(of_type_exact(str, type(None)))],
        parameters=[optional(of_type_exact(Parameter, type(None)))]
    )
    def __init__(
        self, button=None, buttons=None, product_retailer_id=None,
        catalog_id=None, sections=None, name=None, parameters=None
    ):
        self.button = button
        self.buttons = buttons if buttons is not None else []
        self.product_retailer_id = product_retailer_id
        self.catalog_id = catalog_id
        self.sections = sections if sections is not None else []
        self.name = name
        self.parameters = parameters


class Interactive:
    @validate_args(
        type=[optional(of_type_exact(str, type(None)))],
        header=[optional(of_type_exact(Header, type(None)))],
        body=[optional(of_type_exact(Body, type(None)))],
        footer=[optional(of_type_exact(Footer, type(None)))],
        action=[optional(of_type_exact(Action, type(None)))]
    )
    def __init__(self, type=None, header=None, body=None, footer=None, action=None):
        self.type = type
        self.header = header
        self.body = body
        self.footer = footer
        self.action = action
