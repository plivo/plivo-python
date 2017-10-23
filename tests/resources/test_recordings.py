# -*- coding: utf-8 -*-

from datetime import datetime

import plivo
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class RecordingTest(PlivoResourceTestCase):
    @with_response(200)
    def test_list(self):
        recordings = self.client.recordings.list(
            add_time__gt=datetime(2017, 4, 15, 1, 1, 1),
            add_time__gte=datetime(2017, 4, 15, 1, 1, 1),
            add_time__lt=datetime(2017, 4, 15, 1, 1, 1),
            add_time__lte=datetime(2017, 4, 15, 1, 1, 1, 123))

        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(recordings)), 3)

        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Recording/?add_time__gt=2017-04-15+01%3A01%3A01&add_time__lt=2017-04-15+01%3A01%3A01&add_time__gte=2017-04-15+01%3A01%3A01&add_time__lte=2017-04-15+01%3A01%3A01.000123&limit=20&offset=0',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('fc2716b0-1c8b-11e4-bwad-842b2b17453e',
                         recordings.objects[1].id)

        with self.assertRaises(plivo.exceptions.ValidationError):
            recordings = self.client.recordings.list(limit=100)

    def test_recording_list_by_subaccount(self):
        expected_response = {
            'account':
            '/v1/Account/MANWVLYTK4ZWU1YTY4ZT/',
            'api_id':
            '323972b2-0db3-11e4-a2d1-22000ac5040c',
            'auth_id':
            'SAXXXXXXXXXXXXXXXXXX',
            'auth_token':
            'MTZjYWM0YzVjNjMwZmVmODFiNWJjNWJmOGJjZjgw',
            'created':
            '2014-07-17',
            'enabled':
            False,
            'modified':
            None,
            'name':
            'Chewbacca',
            'resource_uri':
            '/v1/Account/MANWVLYTK4ZWU1YTY4ZT/Subaccount/SAMTVIYJDIYWYYMZHLYZ/'
        }

        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        account_details = self.client.subaccounts.get('SA' + 'X' * 18)

        expected_response = {
            'api_id': 'ff25223a-1c9f-11e4-80aa-12313f048015',
            'meta': {
                'limit':
                3,
                'next':
                '/v1/Account/MANWVLYTK4ZWU1YTY4ZT/Recording/?limit=3&offset=3',
                'offset':
                0,
                'previous':
                None,
                'total_count':
                948
            },
            'objects': []
        }

        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        with self.assertRaises(plivo.exceptions.ValidationError):
            recordings = self.client.recordings.list(
                subaccount='SA' + 'X' * 17)

        recordings = self.client.recordings.list(
            subaccount='SA' + 'X' * 18, call_uuid='SomeCallUUID')

        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Recording/?call_uuid=SomeCallUUID&limit=20&subaccount=SAXXXXXXXXXXXXXXXXXX&offset=0',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        with self.assertRaises(plivo.exceptions.ValidationError):
            recordings = self.client.recordings.list(limit=100)

        recordings = self.client.recordings.list(
            subaccount=account_details, call_uuid='SomeCallUUID')

        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Recording/?call_uuid=SomeCallUUID&limit=20&subaccount=SAXXXXXXXXXXXXXXXXXX&offset=0',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    @with_response(200)
    def test_get(self):

        recording = self.client.recordings.get(
            'c2186400-1c8c-11e4-a664-0026b945b52x')

        self.assertResponseMatches(recording)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Recording/c2186400-1c8c-11e4-a664-0026b945b52x/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        # Verifying the object type returned
        self.assertEqual(plivo.resources.recordings.Recording,
                         recording.__class__)

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('c2186400-1c8c-11e4-a664-0026b945b52x', recording.id)

        self.assertEqual('345100.00000', recording.recording_duration_ms)

    @with_response(204)
    def test_delete(self):

        response = self.client.recordings.delete(
            'c2186400-1c8c-11e4-a664-0026b945b52x')

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Recording/c2186400-1c8c-11e4-a664-0026b945b52x/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('DELETE', self.client.current_request.method)
