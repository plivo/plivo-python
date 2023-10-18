from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class VerifyCalleridTest(PlivoResourceTestCase):
    @with_response(201)
    def test_initiate(self):
        self.client.verify_callerids.initiate_verify(phone_number='917708772011',
                                                     alias='test',
                                                     channel='call')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('VerifiedCallerId'), self.client.current_request.url)

    @with_response(201)
    def test_verify(self):
        verification_uuid = 'eeab1477-e59b-4821-9e61-fd5847c2a5db'
        self.client.verify_callerids.verify_caller_id(
            verification_uuid='eeab1477-e59b-4821-9e61-fd5847c2a5db', otp='610534')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('VerifiedCallerId', 'Verification', verification_uuid), self.client.current_request.url)

    @with_response(200)
    def test_delete(self):
        phone_number = "917708772011"
        self.client.verify_callerids.delete_verified_caller_id(
            phone_number)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_voice_url('VerifiedCallerId', phone_number), self.client.current_request.url)

    @with_response(200)
    def test_get(self):
        phone_number = "917708772011"
        self.client.verify_callerids.get_verified_caller_id(phone_number)
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.get_voice_url('VerifiedCallerId', phone_number), self.client.current_request.url)

    @with_response(200)
    def test_update(self):
        phone_number = "917708772011"
        self.client.verify_callerids.update_verified_caller_id(
            phone_number=phone_number,
            alias='test123')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('VerifiedCallerId', phone_number), self.client.current_request.url)

    @with_response(200)
    def test_list(self):
        self.client.verify_callerids.list_verified_caller_id()
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.get_voice_url('VerifiedCallerId'), self.client.current_request.url)
