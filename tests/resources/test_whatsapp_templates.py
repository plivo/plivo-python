# -*- coding: utf-8 -*-
from tests.base import PlivoResourceTestCase


class WhatsappTemplateTest(PlivoResourceTestCase):

    def test_create_template(self):
        expected_response = {
            'api_id': 'api-id-xxx',
            'template_id': 'tmpl-001',
            'template_name': 'my_template',
            'template_status': 'PENDING',
            'template_category': 'MARKETING',
            'template_language': 'en_US',
            'status': 'success',
            'message': 'Template created',
        }
        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.whatsapp_templates.create(
            waba_id='waba-001',
            name='my_template',
            category='MARKETING',
            language='en_US',
            components=[{'type': 'BODY', 'text': 'Hello'}],
            allow_category_change=True,
        )

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('WhatsApp', 'Template', 'waba-001'))
        self.assertEqual(self.client.current_request.method, 'POST')

    def test_update_template(self):
        expected_response = {
            'api_id': 'api-id-xxx',
            'template_id': 'tmpl-001',
            'template_name': 'my_template',
            'template_status': 'PENDING',
            'template_category': 'UTILITY',
            'template_language': 'en_US',
            'status': 'success',
            'message': 'Template updated',
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.whatsapp_templates.update(
            waba_id='waba-001',
            template_id='tmpl-001',
            category='UTILITY',
        )

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('WhatsApp', 'Template', 'waba-001', 'tmpl-001'))
        self.assertEqual(self.client.current_request.method, 'POST')

    def test_get_template(self):
        expected_response = {
            'api_id': 'api-id-xxx',
            'template_id': 'tmpl-001',
            'name': 'my_template',
            'category': 'MARKETING',
            'language': 'en_US',
            'status': 'APPROVED',
            'components': [{'type': 'BODY', 'text': 'Hello'}],
            'quality_score': {'score': 'GREEN'},
            'rejected_reason': None,
            'message': None,
            'error': None,
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.whatsapp_templates.get(
            waba_id='waba-001',
            template_id='tmpl-001',
        )

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('WhatsApp', 'Template', 'waba-001', 'tmpl-001'))
        self.assertEqual(self.client.current_request.method, 'GET')

    def test_list_templates(self):
        expected_response = {
            'api_id': 'api-id-xxx',
            'objects': [
                {'template_id': 'tmpl-001', 'name': 'my_template'},
                {'template_id': 'tmpl-002', 'name': 'other_template'},
            ],
            'meta': {'total_count': 2, 'limit': 20, 'offset': 0},
            'status': 'success',
            'message': None,
            'error': None,
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.whatsapp_templates.list(
            waba_id='waba-001',
            template_name='my_template',
            limit=20,
            offset=0,
        )

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('WhatsApp', 'Template', 'waba-001'))
        self.assertEqual(self.client.current_request.method, 'GET')

    def test_delete_template(self):
        self.client.set_expected_response(status_code=204, data_to_return={})

        self.client.whatsapp_templates.delete(
            waba_id='waba-001',
            template_id='tmpl-001',
            name='my_template',
        )

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('WhatsApp', 'Template', 'waba-001', 'tmpl-001'))
        self.assertEqual(self.client.current_request.method, 'DELETE')