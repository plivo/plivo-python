# -*- coding: utf-8 -*-
from plivo import exceptions
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class SessionTest(PlivoResourceTestCase):
    def test_create_session(self):
        expected_response = {'session_uuid': 'adsdafkjadshf123123'}
        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        test_session = self.client.verify_session.create(
            recipient='1234567890')

        self.assertEqual(
            self.client.current_request.url,
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Verify/Session/')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(test_session.session_uuid,
                         expected_response['session_uuid'])

    def test_create_session_without_recipient(self):
        self.assertRaises(
            exceptions.ValidationError,
            self.client.verify_session.create
        )

    @with_response(200)
    def test_get(self):
        session_uuid = 'session_uuid'
        session = self.client.verify_session.get(session_uuid)
        self.assertResponseMatches(session)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Verify', 'Session', session_uuid))
        self.assertEqual(self.client.current_request.method, 'GET')

    @with_response(200)
    def test_list(self):
        messages = self.client.verify_session.list()
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(messages)), 20)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Verify', 'Session'))
        self.assertEqual(self.client.current_request.method, 'GET')

    @with_response(200)
    def test_validate(self):
        session_uuid = '1234567'
        expected_response = {'message': 'session validated successfully.'}
        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        test_session = self.client.verify_session.validate(
            session_uuid=session_uuid, otp='123456')

        self.assertEqual(
            self.client.current_request.url,
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Verify/Session/1234567/')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(test_session.message,
                         expected_response['message'])

