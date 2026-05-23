# -*- coding: utf-8 -*-
from tests.base import PlivoResourceTestCase


class VerifyAppTest(PlivoResourceTestCase):
    def test_create_verify_app(self):
        expected_response = {
            'api_id': 'some-api-id',
            'app_uuid': 'some-app-uuid',
            'message': 'Verify app created',
        }
        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.verify_apps.create(name='TestApp')

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App'))
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(response.app_uuid, expected_response['app_uuid'])

    def test_create_verify_app_with_all_params(self):
        expected_response = {
            'api_id': 'some-api-id',
            'app_uuid': 'some-app-uuid',
            'message': 'Verify app created',
        }
        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.verify_apps.create(
            name='TestApp',
            brand_name='MyBrand',
            otp_type='numeric',
            otp_length=6,
            otp_expiry=300,
            otp_attempts=3,
            max_validation_attempts=5,
            sms_channel=True,
            voice_channel=False,
            wa_channel=False,
            is_default=False,
            message_redaction=False,
            enable_fraudshield=False,
            number_pool='pool-id',
        )

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(response.app_uuid, expected_response['app_uuid'])

    def test_list_verify_apps(self):
        expected_response = {
            'api_id': 'some-api-id',
            'verify_apps': [
                {'app_uuid': 'uuid-1', 'name': 'App1'},
                {'app_uuid': 'uuid-2', 'name': 'App2'},
            ],
            'meta': {'limit': 20, 'offset': 0, 'total_count': 2},
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_apps.list()

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App'))
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertEqual(len(list(response)), 2)

    def test_list_verify_apps_with_filters(self):
        expected_response = {
            'api_id': 'some-api-id',
            'verify_apps': [
                {'app_uuid': 'uuid-1', 'name': 'App1'},
            ],
            'meta': {'limit': 20, 'offset': 0, 'total_count': 1},
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_apps.list(
            name='App1',
            limit=20,
            offset=0,
        )

        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertEqual(len(list(response)), 1)

    def test_list_templates(self):
        expected_response = {
            'api_id': 'some-api-id',
            'templates': [
                {'template_uuid': 'tmpl-1', 'name': 'Default OTP'},
            ],
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_apps.list_templates()

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App', 'templates'))
        self.assertEqual(self.client.current_request.method, 'GET')

    def test_get_verify_app(self):
        app_uuid = 'some-app-uuid'
        expected_response = {
            'api_id': 'some-api-id',
            'verify_app': {'app_uuid': app_uuid, 'name': 'TestApp'},
            'verify_whatsapp': None,
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_apps.get(app_uuid)

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App', app_uuid))
        self.assertEqual(self.client.current_request.method, 'GET')

    def test_update_verify_app(self):
        app_uuid = 'some-app-uuid'
        expected_response = {
            'api_id': 'some-api-id',
            'app_uuid': app_uuid,
            'message': 'Verify app updated',
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_apps.update(
            app_uuid, name='UpdatedName', otp_length=4)

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App', app_uuid))
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(response.app_uuid, app_uuid)

    def test_delete_verify_app(self):
        app_uuid = 'some-app-uuid'
        self.client.set_expected_response(status_code=204, data_to_return={})

        self.client.verify_apps.delete(app_uuid)

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'App', app_uuid))
        self.assertEqual(self.client.current_request.method, 'DELETE')