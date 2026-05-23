# -*- coding: utf-8 -*-
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class VerifySessionTest(PlivoResourceTestCase):

    def test_create_session_minimal(self):
        expected_response = {'session_uuid': 'abc123sessionuuid', 'api_id': 'some-api-id'}
        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.verify_session.create()

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'Session'))
        self.assertEqual(self.client.current_request.method, 'POST')

    def test_create_session_with_all_params(self):
        expected_response = {'session_uuid': 'abc123sessionuuid', 'api_id': 'some-api-id'}
        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.verify_session.create(
            app_hash='app_hash_value',
            brand_name='MyBrand',
            code_length=6,
            dlt_entity_id='entity123',
            dlt_sender_id='sender123',
            dlt_template_category='transactional',
            dlt_template_id='template123',
            dlt_text='Your OTP is {otp}',
            dtmf=1,
            fraud_check='medium',
            text='Your OTP is {otp}. Valid for 10 minutes.',
        )

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'Session'))
        self.assertEqual(self.client.current_request.method, 'POST')

    def test_get_session(self):
        expected_response = {'session_uuid': 'abc123sessionuuid', 'api_id': 'some-api-id', 'status': 'otp_sent'}
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        session_uuid = 'abc123sessionuuid'
        response = self.client.verify_session.get(session_uuid)

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'Session', session_uuid))
        self.assertEqual(self.client.current_request.method, 'GET')

    def test_list_sessions(self):
        expected_response = {
            'api_id': 'some-api-id',
            'sessions': [],
            'meta': {'limit': 20, 'offset': 0, 'total_count': 0, 'next': None, 'previous': None},
        }
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        response = self.client.verify_session.list()

        self.assertUrlEqual(
            self.client.current_request.url,
            self.get_url('Verify', 'Session'))
        self.assertEqual(self.client.current_request.method, 'GET')