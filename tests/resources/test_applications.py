# -*- coding: utf-8 -*-

import plivo
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class ApplicationTest(PlivoResourceTestCase):
    def test_application_create_invalid_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.applications.create(None, None)

        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.applications.create('None', None)

        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.applications.create(
                answer_url='None',
                app_name='None',
                hangup_url='None',
                fallback_answer_url='None',
                message_url='None',
                default_number_app=True,
                default_endpoint_app=True,
                subaccount='SAXXXXXXXXXXXXXXXXX')

    def test_application_create_with_subaccount_object(self):
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
            'message': 'created',
            'app_id': '15784735442685051',
            'api_id': '5a9fcb68-582d-11e1-86da-6ff39efcb949'
        }

        self.client.set_expected_response(
            status_code=201, data_to_return=expected_response)

        response = self.client.applications.create(
            answer_url='None',
            app_name='None',
            hangup_url='None',
            fallback_answer_url='None',
            message_url='None',
            default_number_app=True,
            default_endpoint_app=True,
            subaccount=account_details)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

    @with_response(201)
    def test_create(self):

        response = self.client.applications.create(
            answer_url='None',
            app_name='None',
            hangup_url='None',
            fallback_answer_url='None',
            message_url='None',
            default_number_app=True,
            default_endpoint_app=True,
            subaccount='SAXXXXXXXXXXXXXXXXXX')

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

    def test_application_get_invalid_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.applications.get(None)

    @with_response(200)
    def test_get(self):

        application = self.client.applications.get(20468599130939380)

        self.assertResponseMatches(application)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/20468599130939380/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        # Verifying the object type returned
        self.assertEqual(plivo.resources.applications.Application,
                         application.__class__)

        self.assertEqual('20468599130939380', application.id)
        self.assertEqual('20468599130939380', application.app_id)

    def test_application_delete_invalid_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.applications.delete(None)

    def test_application_delete(self):
        expected_response = {}

        self.client.set_expected_response(
            status_code=204, data_to_return=expected_response)

        response = self.client.applications.delete(20372631212782780)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/20372631212782780/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('DELETE', self.client.current_request.method)

    def test_application_update_invalid_params(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.applications.update(None, 'None', 'None')

        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.applications.update('AppId', None, None, None, None,
                                            None, None, None, None, None, None,
                                            None)

        with self.assertRaises(plivo.exceptions.ValidationError):
            self.client.applications.update('AppId', None, None, None, None,
                                            None, None, None, None, None, None,
                                            'SAXXXXXXXXXXXXXXXXX')

    def test_application_update(self):
        expected_response = {
            'message': 'changed',
            'api_id': '5a9fcb68-582d-11e1-86da-6ff39efcb949'
        }

        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        updated_app = self.client.applications.update(
            app_id='20372631212782780',
            answer_url='https://example.com',
            hangup_url='https://example.com',
            fallback_answer_url='https://example.com',
            message_url='https://example.com',
            default_number_app=True,
            default_endpoint_app=True,
            subaccount='SAXXXXXXXXXXXXXXXXXX')

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/20372631212782780/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

    def test_application_update_with_subaccount_object(self):
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
            'api_id': '5a9fcb68-582d-11e1-86da-6ff39efcb949'
        }

        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        updated_app = self.client.applications.update(
            app_id='20372631212782780',
            answer_url='https://example.com',
            hangup_url='https://example.com',
            fallback_answer_url='https://example.com',
            message_url='https://example.com',
            default_number_app=True,
            default_endpoint_app=True,
            subaccount=account_details)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/20372631212782780/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

    def test_application_update_by_object(self):
        expected_response = {
            'answer_method':
            'GET',
            'answer_url':
            'http://webapp.com/dial.xml',
            'app_id':
            '20372631212782780',
            'app_name':
            'Dial Office',
            'default_app':
            False,
            'enabled':
            True,
            'fallback_answer_url':
            '',
            'fallback_method':
            'POST',
            'hangup_method':
            'POST',
            'hangup_url':
            'http://webapp.com/dial.xml',
            'message_method':
            'POST',
            'message_url':
            '',
            'public_uri':
            False,
            'resource_uri':
            '/v1/Account/MANWVLYTK4ZWU1YTY4ZT/Application/20372631212782780/',
            'sip_uri':
            'sip:20372631212782780@app.plivo.com',
            'sub_account':
            None
        }

        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        application = self.client.applications.get(20372631212782780)

        expected_response = {
            'message': 'changed',
            'api_id': '5a9fcb68-582d-11e1-86da-6ff39efcb949'
        }

        self.client.set_expected_response(
            status_code=202, data_to_return=expected_response)

        update_resp = application.update(
            answer_url='https://example.com/plivo.xml',
            hangup_url='https://example.com/plivo.xml',
            fallback_answer_url='https://example.com/plivo.xml',
            message_url='https://example.com/plivo.xml',
            default_number_app=True,
            default_endpoint_app=True,
            subaccount='SAXXXXXXXXXXXXXXXXXX')

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/20372631212782780/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

        self.assertEqual('20372631212782780', application.id)
        self.assertEqual('20372631212782780', application.app_id)
        self.assertEqual('https://example.com/plivo.xml',
                         application.answer_url)

    def test_application_list(self):
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
            'api_id':
            'e5b05b26-10c4-11e4-a2d1-22000ac5040c',
            'meta': {
                'limit': 20,
                'next': None,
                'offset': 0,
                'previous': None,
                'total_count': 2
            },
            'objects': [{
                'answer_url':
                'http://webapp.com/dial.xml',
                'answer_method':
                'GET',
                'app_id':
                '20372631212782780',
                'app_name':
                'Dial Office',
                'default_app':
                False,
                'enabled':
                True,
                'fallback_answer_url':
                '',
                'fallback_method':
                'POST',
                'hangup_method':
                'POST',
                'hangup_url':
                'http://webapp.com/dial.xml',
                'message_method':
                'POST',
                'message_url':
                '',
                'public_uri':
                False,
                'resource_uri':
                '/v1/Account/MANWVLYTK4ZWU1YTY4ZT/Application/20372631212782780/',
                'sip_uri':
                'sip:20372631212782780@app.plivo.com',
                'sub_account':
                None
            }, {
                'answer_url':
                'https://webapp.com/conference_court.xml',
                'answer_method':
                'GET',
                'app_id':
                '14260623927192078',
                'app_name':
                'Conference_Court',
                'default_app':
                False,
                'enabled':
                True,
                'fallback_answer_url':
                '',
                'fallback_method':
                'POST',
                'hangup_method':
                'POST',
                'hangup_url':
                'https://webapp.com/conference_court.xml',
                'message_method':
                'POST',
                'message_url':
                '',
                'public_uri':
                False,
                'resource_uri':
                '/v1/Account/MANWVLYTK4ZWU1YTY4ZT/Application/14260623927192078/',
                'sip_uri':
                'sip:142606239271920703@app.plivo.com',
                'sub_account':
                None
            }]
        }

        self.client.set_expected_response(
            status_code=200, data_to_return=expected_response)

        applications = self.client.applications.list(offset=10, limit=10)

        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/?limit=10&offset=10',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        self.assertEqual('20372631212782780', applications.objects[0].id)
        self.assertEqual('14260623927192078', applications.objects[-1].app_id)

        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(applications)), 2)

        applications = self.client.applications.list(
            offset=10, limit=10, subaccount='SAXXXXXXXXXXXXXXXXXX')

        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/?limit=10&subaccount=SAXXXXXXXXXXXXXXXXXX&offset=10',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        self.assertEqual('20372631212782780', applications.objects[0].id)
        self.assertEqual('14260623927192078', applications.objects[-1].app_id)

        applications = self.client.applications.list(
            offset=10, limit=10, subaccount=account_details)

        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Application/?limit=10&subaccount=SAXXXXXXXXXXXXXXXXXX&offset=10',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        self.assertEqual('20372631212782780', applications.objects[0].id)
        self.assertEqual('14260623927192078', applications.objects[-1].app_id)

        with self.assertRaises(plivo.exceptions.ValidationError):
            applications = self.client.applications.list(
                offset=10, limit=10, subaccount='SAXXXXXXXXXXXXX d')

        with self.assertRaises(plivo.exceptions.ValidationError):
            applications = self.client.applications.list(offset=10, limit=100)
