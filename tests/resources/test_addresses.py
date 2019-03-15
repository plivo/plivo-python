# -*- coding: utf-8 -*-

import plivo

from tests.base import PlivoResourceTestCase
from tests.decorators import with_response

address_id = '20220771838737'


class AddressTest(PlivoResourceTestCase):
    @with_response(200)
    def test_list(self):
        addresses = self.client.addresses.list()
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(addresses)), 1)

        print(self.client.current_request.url)

        # Verifying the endpoint hit
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url(
                                'Verification', 'Address', limit=20, offset=0))

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    def test_addresses_list_all_invalid_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            addresses = self.client.addresses.list(limit=100)

    @with_response(200)
    def test_get(self):
        address = self.client.addresses.get(address_id)
        self.assertResponseMatches(address)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Verification', 'Address',
                                         address_id))
        self.assertEqual(self.client.current_request.method, 'GET')

    @with_response(202)
    def test_update(self):
        self.client.addresses.update(
            address_id,
            salutation='Mr',
            first_name='Bruce',
            last_name='Wayne', )
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Verification', 'Address',
                                         address_id))
        self.assertEqual(self.client.current_request.method, 'POST')

        # Checking the content type
        content_type = self.client.current_request.headers['Content-Type']
        self.assertTrue(
            any([
                'multipart' in content_type, 'www-form-urlencoded' in
                content_type
            ]))

    @with_response(204)
    def test_addresses_delete(self):
        self.client.addresses.delete(address_id)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Verification', 'Address',
                                         address_id))
        self.assertEqual(self.client.current_request.method, 'DELETE')

    @with_response(202)
    def test_create(self):
        self.client.addresses.create(
            country_iso='FR',
            salutation='Mr',
            first_name='Bruce',
            last_name='Wayne',
            address_line1='128',
            address_line2='RUE DU COMMANDANT GUILBAUD',
            city='PARIS',
            region='PARIS',
            postal_code='75016',
            proof_type='others', 
            number_type='local',
            phone_number_country='DE')
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Verification', 'Address'))
        self.assertEqual(self.client.current_request.method, 'POST')

        # Checking the content type
        content_type = self.client.current_request.headers['Content-Type']
        self.assertTrue(
            any([
                'multipart' in content_type, 'www-form-urlencoded' in
                content_type
            ]))
