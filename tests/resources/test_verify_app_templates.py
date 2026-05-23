# -*- coding: utf-8 -*-
from tests.base import PlivoResourceTestCase


class VerifyAppTemplatesTest(PlivoResourceTestCase):
    def test_list(self):
        expected_response = {
            'api_id': 'some-api-id',
            'templates': [
                {
                    'template_uuid': 'uuid-1',
                    'text': 'Your OTP is {{otp}}',
                    'friendly_name': 'Default OTP',
                    'locale': 'en',
                },
                {
                    'template_uuid': 'uuid-2',
                    'text': 'Use {{otp}} to verify',
                    'friendly_name': 'Verify OTP',
                    'locale': 'en',
                },
            ],
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_app_templates.list()

        self.assertEqual(
            self.client.current_request.url,
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Verify/App/templates/')
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertEqual(response.api_id, expected_response['api_id'])
        self.assertEqual(len(response), 2)
        templates = list(response)
        self.assertEqual(templates[0]['template_uuid'], 'uuid-1')
        self.assertEqual(templates[1]['template_uuid'], 'uuid-2')