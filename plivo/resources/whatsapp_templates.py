# -*- coding: utf-8 -*-
from plivo.utils.validators import *

from ..base import PlivoResource, PlivoResourceInterface
from ..exceptions import *
from ..utils import *


class WhatsappTemplate(PlivoResource):
    _name = 'WhatsappTemplate'
    _identifier_string = 'template_id'

    def delete(self):
        return self.client.whatsapp_templates.delete(
            self.__dict__.get('waba_id'), self.id)

    def update(self,
               components=None,
               application_id=None):
        return self.client.whatsapp_templates.update(
            self.__dict__.get('waba_id'),
            self.id,
            components=components,
            application_id=application_id)


class WhatsappTemplates(PlivoResourceInterface):
    _resource_type = WhatsappTemplate

    @validate_args(
        waba_id=[of_type(six.text_type)],
        name=[of_type(six.text_type)],
        language=[of_type(six.text_type)],
        category=[of_type(six.text_type)],
        components=[optional(of_type_exact(list))],
        application_id=[optional(of_type(six.text_type))],
    )
    def create(self,
               waba_id,
               name,
               language,
               category,
               components=None,
               application_id=None):
        return self.client.request(
            'POST',
            ('WhatsApp', 'Template', waba_id),
            to_param_dict(self.create, locals()))

    @validate_args(
        waba_id=[of_type(six.text_type)],
        template_id=[of_type(six.text_type)],
        components=[optional(of_type_exact(list))],
        application_id=[optional(of_type(six.text_type))],
    )
    def update(self,
               waba_id,
               template_id,
               components=None,
               application_id=None):
        return self.client.request(
            'POST',
            ('WhatsApp', 'Template', waba_id, template_id),
            to_param_dict(self.update, locals()))

    @validate_args(
        waba_id=[of_type(six.text_type)],
        template_id=[of_type(six.text_type)],
    )
    def delete(self, waba_id, template_id):
        return self.client.request(
            'DELETE',
            ('WhatsApp', 'Template', waba_id, template_id))

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
    )
    def list(self,
             waba_id,
             limit=None,
             offset=None):
        return self.client.request(
            'GET',
            ('WhatsApp', 'Template', waba_id),
            to_param_dict(self.list, locals()),
            response_type=WhatsappTemplate)