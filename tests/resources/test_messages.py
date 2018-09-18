# -*- coding: utf-8 -*-
from plivo import exceptions
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class MessageTest(PlivoResourceTestCase):
    def test_send_message(self):
        expected_response = {'message_uuid': 'adsdafkjadshf123123'}
        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        test_message = self.client.messages.create(
            src='1234', dst='12345', text='Abcd')

        self.assertEqual(
            self.client.current_request.url,
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Message/')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertEqual(test_message.message_uuid,
                         expected_response['message_uuid'])

    def test_send_message_same_src_dst(self):
        self.assertRaises(
            exceptions.ValidationError,
            self.client.messages.create,
            src='1234',
            dst='1234',
            text='Abcd')

    @with_response(200)
    def test_get(self):
        message_uuid = 'message_uuid'
        message = self.client.messages.get(message_uuid)
        self.assertResponseMatches(message)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Message', message_uuid))
        self.assertEqual(self.client.current_request.method, 'GET')

    @with_response(200, method_name='get')
    def test_response_has_user_agent(self):
        message_uuid = 'message_uuid'
        self.client.messages.get(message_uuid)
        self.assertIn('plivo-python',
                      self.client.current_request.headers['User-Agent'])

    @with_response(200)
    def test_list(self):
        messages = self.client.messages.list()
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(messages)), 20)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Message'))
        self.assertEqual(self.client.current_request.method, 'GET')
