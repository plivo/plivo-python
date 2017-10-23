# -*- coding: utf-8 -*-

import plivo
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response

number_id = '123'


class NumberTest(PlivoResourceTestCase):
    @with_response(200)
    def test_list(self):
        numbers = self.client.numbers.list(
            number_startswith=24,
            services=['voice', 'sms'],
            alias='SomeAlias',
            type='local')
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(numbers)), 3)

        print(self.client.current_request.url)

        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Number/?number_startswith=24&alias=SomeAlias&limit=20&offset=0&services=voice%2Csms&type=local',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    def test_numbers_list_all_invalid_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            numbers = self.client.numbers.list(limit=100)

    @with_response(200)
    def test_get(self):
        number = self.client.numbers.get(number_id)
        self.assertResponseMatches(number)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Number', number_id))
        self.assertEqual(self.client.current_request.method, 'GET')

    @with_response(202)
    def test_update(self):
        self.client.numbers.update(number_id, alias='Test')
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Number', number_id))
        self.assertEqual(self.client.current_request.method, 'POST')

    @with_response(204)
    def test_numbers_delete(self):
        self.client.numbers.delete(number_id)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Number', number_id))
        self.assertEqual(self.client.current_request.method, 'DELETE')

    @with_response(202)
    def test_create(self):
        self.client.numbers.create('1231231231', 'carrier', 'region')
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url(
                                'Number', ))
        self.assertEqual(self.client.current_request.method, 'POST')


class PhoneNumberTest(PlivoResourceTestCase):
    @with_response(200)
    def test_list(self):
        self.client.numbers.search('GB', type='tollfree')
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url(
                                'PhoneNumber',
                                type='tollfree',
                                country_iso='GB'))
        self.assertEqual(self.client.current_request.method, 'GET')

    @with_response(202)
    def test_create(self):
        self.client.numbers.buy(number_id, app_id='test')
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('PhoneNumber', number_id))
        self.assertEqual(self.client.current_request.method, 'POST')
