# -*- coding: utf-8 -*-
from tests.base import PlivoResourceTestCase


class BulkMessageTest(PlivoResourceTestCase):
    def test_create_bulk_message(self):
        expected_response = {
            'api_id': 'api-id-123',
            'message_uuid': ['uuid-1', 'uuid-2'],
            'message': 'requests queued',
        }
        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        response = self.client.bulk_messages.create(
            src='+14155551234',
            dst='+14155550001<+14155550002',
            text='Hello World')

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Message', 'Bulk'))
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(response.message_uuid, expected_response['message_uuid'])

    def test_create_bulk_message_with_optional_params(self):
        expected_response = {
            'api_id': 'api-id-456',
            'message_uuid': ['uuid-3'],
            'message': 'requests queued',
        }
        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        response = self.client.bulk_messages.create(
            src='+14155551234',
            dst='+14155550001',
            text='Hello World',
            type_='sms',
            url='https://example.com/status',
            method='POST',
            log=False,
            powerpack_uuid='some-powerpack-uuid')

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Message', 'Bulk'))
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(response.message_uuid, expected_response['message_uuid'])

    def test_create_bulk_message_with_invalid_numbers(self):
        expected_response = {
            'api_id': 'api-id-789',
            'message_uuid': ['uuid-4'],
            'message': 'requests queued',
            'invalid_number': ['+1invalid'],
        }
        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        response = self.client.bulk_messages.create(
            src='+14155551234',
            dst='+14155550001<+1invalid',
            text='Hello World')

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Message', 'Bulk'))
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(response.invalid_number, expected_response['invalid_number'])