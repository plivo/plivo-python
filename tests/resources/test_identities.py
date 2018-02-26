# -*- coding: utf-8 -*-

import plivo

from tests.base import PlivoResourceTestCase
from tests.decorators import with_response

identity_id = '24856289978366'


class IdentityTest(PlivoResourceTestCase):
    @with_response(200)
    def test_list(self):
        identities = self.client.identities.list()
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(identities)), 1)

        print(self.client.current_request.url)

        # Verifying the endpoint hit
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url(
                                'Verification', 'Identity', limit=20,
                                offset=0))

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

    def test_identities_list_all_invalid_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            identities = self.client.identities.list(limit=100)

    @with_response(200)
    def test_get(self):
        identity = self.client.identities.get(identity_id)
        self.assertResponseMatches(identity)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Verification', 'Identity',
                                         identity_id))
        self.assertEqual(self.client.current_request.method, 'GET')

    @with_response(202)
    def test_update(self):
        self.client.identities.update(
            identity_id,
            country_iso='US',
            salutation='Mr',
            first_name='Bruce',
            last_name='Wayne',
            birth_place='Gotham City',
            birth_date='1900-01-01',
            nationality='New Earth',
            id_nationality='New Earth',
            id_issue_date='2018-01-01',
            id_type='passport',
            id_number='128163264', )
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Verification', 'Identity',
                                         identity_id))
        self.assertEqual(self.client.current_request.method, 'POST')

        # Checking the content type
        content_type = self.client.current_request.headers['Content-Type']
        self.assertTrue(
            any([
                'multipart' in content_type, 'www-form-urlencoded' in
                content_type
            ]))

    @with_response(204)
    def test_identities_delete(self):
        self.client.identities.delete(identity_id)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Verification', 'Identity',
                                         identity_id))
        self.assertEqual(self.client.current_request.method, 'DELETE')

    @with_response(202)
    def test_create(self):
        self.client.identities.create(
            country_iso='US',
            salutation='Mr',
            first_name='Bruce',
            last_name='Wayne',
            birth_place='Gotham City',
            birth_date='1900-01-01',
            nationality='New Earth',
            id_nationality='New Earth',
            id_issue_date='2018-01-01',
            id_type='passport',
            id_number='128163264',
            address_line1='128',
            address_line2='RUE DU COMMANDANT GUILBAUD',
            city='PARIS',
            region='PARIS',
            postal_code='75016', )
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Verification', 'Identity'))
        self.assertEqual(self.client.current_request.method, 'POST')

        # Checking the content type
        content_type = self.client.current_request.headers['Content-Type']
        self.assertTrue(
            any([
                'multipart' in content_type, 'www-form-urlencoded' in
                content_type
            ]))
