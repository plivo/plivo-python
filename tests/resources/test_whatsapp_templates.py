# -*- coding: utf-8 -*-
from tests.base import PlivoResourceTestCase


class WhatsappTemplateTest(PlivoResourceTestCase):

    def test_create_template(self):
        expected_response = {
            'api_id': 'api-id-string',
            'template_id': 'template-uuid-string',
        }
        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.whatsapp_templates.create(
            waba_id='waba-id-string',
            name='test_template',
            language='en_US',
            category='MARKETING',
            components=[{'type': 'BODY', 'text': 'Hello'}])

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('WhatsApp', 'Template', 'waba-id-string'))

    def test_create_template_with_application_id(self):
        expected_response = {
            'api_id': 'api-id-string',
            'template_id': 'template-uuid-string',
        }
        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.whatsapp_templates.create(
            waba_id='waba-id-string',
            name='test_template',
            language='en_US',
            category='MARKETING',
            components=[{'type': 'BODY', 'text': 'Hello'}],
            application_id='app-id-string')

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('WhatsApp', 'Template', 'waba-id-string'))

    def test_update_template(self):
        expected_response = {
            'api_id': 'api-id-string',
            'template_id': 'template-uuid-string',
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.whatsapp_templates.update(
            waba_id='waba-id-string',
            template_id='template-uuid-string',
            components=[{'type': 'BODY', 'text': 'Hello Updated'}])

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('WhatsApp', 'Template', 'waba-id-string',
                         'template-uuid-string'))

    def test_update_template_with_application_id(self):
        expected_response = {
            'api_id': 'api-id-string',
            'template_id': 'template-uuid-string',
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.whatsapp_templates.update(
            waba_id='waba-id-string',
            template_id='template-uuid-string',
            components=[{'type': 'BODY', 'text': 'Hello Updated'}],
            application_id='app-id-string')

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('WhatsApp', 'Template', 'waba-id-string',
                         'template-uuid-string'))

    def test_delete_template(self):
        self.client.set_expected_response(status_code=204, data_to_return={})

        self.client.whatsapp_templates.delete(
            waba_id='waba-id-string',
            template_id='template-uuid-string')

        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('WhatsApp', 'Template', 'waba-id-string',
                         'template-uuid-string'))