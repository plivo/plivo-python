# -*- coding: utf-8 -*-

import plivo
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class TollfreeVerificationTest(PlivoResourceTestCase):
    @with_response(200)
    def test_TollfreeVerificationList(self):
        tollfree_verification = self.client.tollfree_verification.list(offset=10, limit=10)

        # Verifying the endpoint hit
        self.assertUrlEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/TollfreeVerification/?limit=10&offset=10',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        self.assertEqual('312b3119-XXXX-XXXX-XXXX-XXXXXXXXXXXX', tollfree_verification.objects[0].uuid)

        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(tollfree_verification)), 2)

        with self.assertRaises(plivo.exceptions.ValidationError):
            tollfree_verification = self.client.tollfree_verification.list(
                offset=10, limit=10, status='PROCESSING1')

    @with_response(200)
    def test_TollfreeVerificationGet(self):
        tollfree_verficiation = self.client.tollfree_verification.get(tollfree_verification_uuid="312b3119-XXXX-XXXX-XXXX-XXXXXXXXXXXX")

        self.assertResponseMatches(tollfree_verficiation)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/TollfreeVerification/312b3119-XXXX-XXXX-XXXX-XXXXXXXXXXXX/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        # Verifying the object type returned
        self.assertEqual(plivo.resources.tollfree_verification.TollfreeVerification,
                         tollfree_verficiation.__class__)

        self.assertEqual('312b3119-XXXX-XXXX-XXXX-XXXXXXXXXXXX', tollfree_verficiation.uuid)

    @with_response(202)
    def test_TollfreeVerificationUpdate(self):
        updated_app = self.client.tollfree_verification.update(
            extra_data='Testing the update of extra data in python-SDK',)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/TollfreeVerification/312b3119-XXXX-XXXX-XXXX-XXXXXXXXXXXX/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

    def test_numbers_TollfreeVerificationDelete(self):
        expected_response = {}

        self.client.set_expected_response(
            status_code=204, data_to_return=expected_response)

        response = self.client.tollfree_verification.delete(tollfree_verification_uuid="312b3119-XXXX-XXXX-XXXX-XXXXXXXXXXXX")

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/TollfreeVerification/312b3119-XXXX-XXXX-XXXX-XXXXXXXXXXXX/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('DELETE', self.client.current_request.method)

    @with_response(202)
    def test_TollfreeVerificationCreate(self):
        response = self.client.tollfree_verification.create(
         usecase="2FA",
         number="18554950186",
         profile_uuid="42f92135-6ec2-4110-8da4-71171f6aad44",
         optin_type="VERBAL",
         volume="100",
         usecase_summary="hbv",
         message_sample="message_sample",
         callback_url="https://plivobin-prod-usw1.plivops.com/1pcfjrt1",
         callback_method="POST",
         optin_image_url="http://aaa.com",
         additional_information="this is additional_information",
         extra_data="this is extra_data",
        )

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/TollfreeVerification/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)