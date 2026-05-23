# -*- coding: utf-8 -*-
from tests.base import PlivoResourceTestCase


class RcsAssistantEventsTest(PlivoResourceTestCase):
    def test_create(self):
        expected_response = {
            'api_id': 'test-api-id',
            'phone_number': '+14155551234',
            'is_capable': True,
            'features': ['RICHCARD_STANDALONE', 'ACTION_CREATE_CALENDAR_EVENT'],
            'message': 'RCS assistant event sent successfully.',
            'error': None,
        }
        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        response = self.client.rcs_assistant_events.create()

        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('RCS', 'AssistantEvents'),
        )
        self.assertEqual(response.api_id, expected_response['api_id'])
        self.assertEqual(response.phone_number, expected_response['phone_number'])
        self.assertEqual(response.is_capable, expected_response['is_capable'])
        self.assertEqual(response.features, expected_response['features'])
        self.assertEqual(response.message, expected_response['message'])
        self.assertEqual(response.error, expected_response['error'])