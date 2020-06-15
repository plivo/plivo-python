# -*- coding: utf-8 -*-

import plivo
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class SubaccountTest(PlivoResourceTestCase):
    def test_subaccount_create_wrong_param(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.subaccounts.create(name=1, enabled=1)

        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.subaccounts.create(name=None)

    def test_subaccount_create(self):
        expected_response = {
            'api_id': '324a7dd8-0db2-11e4-8a4a-123140008edf',
            'auth_id': 'SAXXXXXXXXXXXXXXXXXX',
            'auth_token': 'MTZjYWM0YzVjNjMwZmVmODFiNWJjNPJmOGJjZjgw',
            'message': 'created'
        }

        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        subaccount = self.client.subaccounts.create(name='TestSAccount')

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Subaccount/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('SAXXXXXXXXXXXXXXXXXX', subaccount.id)
        self.assertEqual('SAXXXXXXXXXXXXXXXXXX', subaccount.auth_id)

    @with_response(200)
    def test_get(self):
        account_details = self.client.subaccounts.get('SAXXXXXXXXXXXXXXXXXX')

        self.assertResponseMatches(account_details)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Subaccount/SAXXXXXXXXXXXXXXXXXX/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('SAODNKNDDMY2EXY2JKMG', account_details.id)

        # Verifying if the parsing was done Pythonically!
        self.assertEqual(False, account_details.enabled)

    def test_subaccount_get_wrong_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.subaccounts.get('MAXXXXXXXXXXXXXXXXXX')

    def test_subaccount_update_wrong_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.subaccounts.update('MAXXXXXXXXXXXXXXXXXX',
                                           'TestSubAcc')

        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.subaccounts.update('SAXXXXXXXXXXXXXXXXXX', None)

        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.subaccounts.update('SAXXXXXXXXXXXXXXXXXX',
                                           'TestSubAcc', 1)

    @with_response(202)
    def test_update(self):

        update_response = self.client.subaccounts.update(
            auth_id='SAXXXXXXXXXXXXXXXXXX',
            name='SherlockHolmes',
            enabled=True)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Subaccount/SAXXXXXXXXXXXXXXXXXX/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('changed', update_response.message)

    def test_subaccount_object_update(self):
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

        account_details = self.client.subaccounts.get('SAXXXXXXXXXXXXXXXXXX')

        expected_response = {
            'message': 'changed',
            'api_id': '5a9fcb68-523d-11e1-86da-6ff39efcb949'
        }

        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        update_response = self.client.subaccounts.update(
            auth_id='SAXXXXXXXXXXXXXXXXXX',
            name='SherlockHolmes',
            enabled=True)

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('changed', update_response.message)

    @with_response(204)
    def test_delete(self):
        subaccount_delete_response = self.client.subaccounts.delete(
            'SAXXXXXXXXXXXXXXXXXX')

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Subaccount/SAXXXXXXXXXXXXXXXXXX/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('DELETE', self.client.current_request.method)

        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.subaccounts.delete('SAXXXXXXXXXXXXXXXXX')

        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.subaccounts.delete('MAXXXXXXXXXXXXXXXXXX')

    @with_response(200)
    def test_list(self):
        subaccounts = self.client.subaccounts.list(offset=10, limit=10)

        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Subaccount/?limit=10&offset=10',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('SANDLHYZBIZMU4ZDEXNM', subaccounts.objects[-1].id)

        # Verifying if the parsing was done Pythonically!
        self.assertEqual(False, subaccounts.objects[0].enabled)

        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(subaccounts)), 3)

        with self.assertRaises(plivo.exceptions.ValidationError):
            subaccounts = self.client.subaccounts.list(offset=10, limit=100)
