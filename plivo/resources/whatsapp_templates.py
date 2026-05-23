# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import PlivoResource, PlivoResourceInterface, ResponseObject
from ..exceptions import *
from ..utils import *


class WhatsappTemplate(PlivoResource):
    _name = 'WhatsappTemplate'
    _identifier_string = 'template_id'

    def get(self):
        return self.client.whatsapp_templates.get(self.waba_id, self.id)

    def update(self,
               name=None,
               category=None,
               language=None,
               components=None,
               allow_category_change=None):
        return self.client.whatsapp_templates.update(
            self.waba_id,
            self.id,
            name=name,
            category=category,
            language=language,
            components=components,
            allow_category_change=allow_category_change)

    def delete(self, name):
        return self.client.whatsapp_templates.delete(self.waba_id, self.id, name)


class WhatsappTemplates(PlivoResourceInterface):
    _resource_type = WhatsappTemplate

    @validate_args(
        waba_id=[of_type(six.text_type)],
        name=[optional(of_type(six.text_type))],
        category=[optional(of_type(six.text_type))],
        language=[optional(of_type(six.text_type))],
        components=[optional(of_type_exact(list))],
        allow_category_change=[optional(of_type_exact(bool))],
    )
    def create(self,
               waba_id,
               name=None,
               category=None,
               language=None,
               components=None,
               allow_category_change=None):
        return self.client.request(
            'POST',
            ('WhatsApp', 'Template', waba_id),
            to_param_dict(self.create, locals()))

    @validate_args(
        waba_id=[of_type(six.text_type)],
        template_id=[of_type(six.text_type)],
        name=[optional(of_type(six.text_type))],
        category=[optional(of_type(six.text_type))],
        language=[optional(of_type(six.text_type))],
        components=[optional(of_type_exact(list))],
        allow_category_change=[optional(of_type_exact(bool))],
    )
    def update(self,
               waba_id,
               template_id,
               name=None,
               category=None,
               language=None,
               components=None,
               allow_category_change=None):
        return self.client.request(
            'POST',
            ('WhatsApp', 'Template', waba_id, template_id),
            to_param_dict(self.update, locals()))

    @validate_args(
        waba_id=[of_type(six.text_type)],
        template_id=[of_type(six.text_type)],
    )
    def get(self, waba_id, template_id):
        return self.client.request(
            'GET',
            ('WhatsApp', 'Template', waba_id, template_id),
            response_type=WhatsappTemplate)

    @validate_args(
        waba_id=[of_type(six.text_type)],
        template_name=[optional(of_type(six.text_type))],
        limit=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda limit: 0 < limit <= 20, '0 < limit <= 20')))
        ],
        offset=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda offset: 0 <= offset, '0 <= offset')))
        ],
    )
    def list(self,
             waba_id,
             template_name=None,
             limit=None,
             offset=None):
        return self.client.request(
            'GET',
            ('WhatsApp', 'Template', waba_id),
            to_param_dict(self.list, locals()))

    @validate_args(
        waba_id=[of_type(six.text_type)],
        template_id=[of_type(six.text_type)],
        name=[of_type(six.text_type)],
    )
    def delete(self, waba_id, template_id, name):
        return self.client.request(
            'DELETE',
            ('WhatsApp', 'Template', waba_id, template_id),
            to_param_dict(self.delete, locals()))