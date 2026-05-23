# -*- coding: utf-8 -*-
from tests.base import PlivoResourceTestCase


class RcsCapabilityTest(PlivoResourceTestCase):
    def test_check_rcs_capability(self):
        expected_response = {
            'api_id': 'some-api-id',
            'phone_number': '+14151234567',
            'is_capable': True,
            'features': ['CHAT', 'FILE_TRANSFER'],
            'message': 'Number is RCS capable.',
            'error': None,
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.rcs_capability.check(
            phone_number='+14151234567')

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('RCS', 'Capability'),
        )
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertEqual(response.phone_number, expected_response['phone_number'])
        self.assertEqual(response.is_capable, expected_response['is_capable'])
        self.assertEqual(response.features, expected_response['features'])

    def test_check_rcs_capability_with_agent_uuid(self):
        expected_response = {
            'api_id': 'some-api-id',
            'phone_number': '+14151234567',
            'is_capable': False,
            'features': [],
            'message': 'Number is not RCS capable.',
            'error': None,
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.rcs_capability.check(
            phone_number='+14151234567',
            agent_uuid='some-agent-uuid')

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('RCS', 'Capability'),
        )
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertEqual(response.is_capable, expected_response['is_capable'])

    def test_check_rcs_capability_missing_phone_number(self):
        from plivo.exceptions import ValidationError
        self.assertRaises(
            (ValidationError, TypeError),
            self.client.rcs_capability.check,
        )