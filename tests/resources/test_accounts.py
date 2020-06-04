# -*- coding: utf-8 -*-

import plivo
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class AccountTest(PlivoResourceTestCase):
    @with_response(200)
    def test_get(self):
        account_details = self.client.account.get()

        self.assertResponseMatches(account_details)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        # Verifying the object type returned
        self.assertEqual(plivo.resources.accounts.Account,
                         account_details.__class__,
                         'Expected an Account class')

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('MAXXXXXXXXXXXXXXXXXX', account_details.id)

        # Verifying if the parsing was done Pythonically!
        self.assertEqual(False, account_details.auto_recharge)

    def test_account_update_no_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.account.update()

        expected_response = {
            'account_type': 'standard',
            'address': '340 Pine St, San Francisco, CA - 94104',
            'api_id': 'c31b36be-0da2-11e4-bd8a-12313f016a39',
            'auth_id': 'MAXXXXXXXXXXXXXXXXXX',
            'auto_recharge': True,
            'billing_mode': 'prepaid',
            'cash_credits': '23.167',
            'city': 'San Francisco',
            'name': 'Han Solo',
            'resource_uri': '/v1/Account/MAXXXXXXXXXXXXXXXXXX/',
            'state': 'California',
            'timezone': 'America/Los_Angeles'
        }

        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        account_details = self.client.account.get()

        with self.assertRaises(plivo.exceptions.ValidationError):
            account_details.update()

    @with_response(202)
    def test_update(self):
        updated_response = self.client.account.update(
            name='Sherlock Holmes',
            city='London',
            address=u'Baker Street, C/o Unicode: తెలుగు')

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('changed', updated_response.message)

    def test_account_object_update(self):
        expected_response = {
            'account_type': 'standard',
            'address': '340 Pine St, San Francisco, CA - 94104',
            'api_id': 'c31b36be-0da2-11e4-bd8a-12313f016a39',
            'auth_id': 'MAXXXXXXXXXXXXXXXXXX',
            'auto_recharge': True,
            'billing_mode': 'prepaid',
            'cash_credits': '23.167',
            'city': 'San Francisco',
            'name': 'Han Solo',
            'resource_uri': '/v1/Account/MAXXXXXXXXXXXXXXXXXX/',
            'state': 'California',
            'timezone': 'America/Los_Angeles'
        }

        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        account_details = self.client.account.get()

        expected_response = {
            'api_id': 'ea43d134-0db0-11e4-a2d1-22000ac5040c',
            'message': 'changed'
        }

        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        update_response = account_details.update(
            name='Sherlock Holmes',
            city='London',
            address=u'Baker Street, C/o Unicode: తెలుగు')

        # Verifying if the Account specific changes and parsing happened
        self.assertEqual('MAXXXXXXXXXXXXXXXXXX', account_details.id)
        self.assertEqual(True, account_details.auto_recharge)
        self.assertEqual('changed', update_response.message)

        # Verifying if the parsing was done Pythonically!
        self.assertEqual(u'Baker Street, C/o Unicode: తెలుగు',
                         account_details.address)
