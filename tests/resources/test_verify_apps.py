# -*- coding: utf-8 -*-
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class VerifyAppTest(PlivoResourceTestCase):

    def test_create_verify_app(self):
        expected_response = {
            'api_id': 'test-api-id',
            'app_uuid': 'test-app-uuid',
            'message': 'Verify app created successfully.',
        }
        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.verify_apps.create(name='TestApp')

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App'))
        self.assertEqual(response.app_uuid, expected_response['app_uuid'])
        self.assertEqual(response.message, expected_response['message'])

    def test_create_verify_app_with_all_params(self):
        expected_response = {
            'api_id': 'test-api-id',
            'app_uuid': 'test-app-uuid',
            'message': 'Verify app created successfully.',
        }
        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.verify_apps.create(
            name='TestApp',
            otp_type='integer',
            otp_length=6,
            otp_expiry=3,
            otp_attempts=3,
            brand_name='MyBrand',
            sms_channel=True,
            voice_channel=False,
            wa_channel=False,
            is_default=False,
            template_uuid='template-uuid',
            message_redaction=False,
            customer_app_hash='abcde12345a',
            max_validation_attempts=5,
            enable_fraudshield=True,
            fs_protection_level='medium',
        )

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(response.app_uuid, expected_response['app_uuid'])

    def test_create_verify_app_with_wa_channel(self):
        expected_response = {
            'api_id': 'test-api-id',
            'app_uuid': 'test-app-uuid-wa',
            'message': 'Verify app created successfully.',
        }
        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.verify_apps.create(
            name='WAApp',
            wa_channel=True,
            waba_id='waba-id-123',
            waba_phone_number='+14155551234',
            waba_template_id='meta-template-id',
        )

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(response.app_uuid, expected_response['app_uuid'])

    def test_list_verify_apps(self):
        expected_response = {
            'api_id': 'test-api-id',
            'meta': {
                'limit': 20,
                'offset': 0,
                'total_count': 1,
                'next': None,
                'previous': None,
            },
            'verify_apps': [
                {'app_uuid': 'test-app-uuid', 'name': 'TestApp'},
            ],
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_apps.list()

        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App'))
        self.assertEqual(len(list(response)), 1)

    def test_list_verify_apps_with_filters(self):
        expected_response = {
            'api_id': 'test-api-id',
            'meta': {
                'limit': 5,
                'offset': 0,
                'total_count': 1,
                'next': None,
                'previous': None,
            },
            'verify_apps': [
                {'app_uuid': 'test-app-uuid', 'name': 'TestApp'},
            ],
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_apps.list(
            name='TestApp',
            channel='sms',
            status='active',
            limit=5,
            offset=0,
        )

        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertEqual(len(list(response)), 1)

    def test_get_verify_app(self):
        app_uuid = 'test-app-uuid'
        expected_response = {
            'api_id': 'test-api-id',
            'verify_app': {
                'app_uuid': app_uuid,
                'name': 'TestApp',
            },
            'verify_whatsapp': None,
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_apps.get(app_uuid)

        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App', app_uuid))

    def test_update_verify_app(self):
        app_uuid = 'test-app-uuid'
        expected_response = {
            'api_id': 'test-api-id',
            'app_uuid': app_uuid,
            'message': 'Verify app updated successfully.',
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_apps.update(
            app_uuid,
            name='UpdatedApp',
            otp_length=8,
        )

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App', app_uuid))
        self.assertEqual(response.app_uuid, expected_response['app_uuid'])

    def test_update_verify_app_with_wa_channel(self):
        app_uuid = 'test-app-uuid'
        expected_response = {
            'api_id': 'test-api-id',
            'app_uuid': app_uuid,
            'message': 'Verify app updated successfully.',
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_apps.update(
            app_uuid,
            wa_channel=True,
            waba_id='waba-id-456',
            waba_phone_number='+14155559999',
            waba_template_id='meta-template-id-2',
        )

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(response.app_uuid, expected_response['app_uuid'])

    def test_delete_verify_app(self):
        app_uuid = 'test-app-uuid'
        expected_response = {
            'api_id': 'test-api-id',
            'app_uuid': app_uuid,
            'message': 'Verify app deleted successfully.',
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        self.client.verify_apps.delete(app_uuid)

        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App', app_uuid))