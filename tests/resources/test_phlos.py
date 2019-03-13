from plivo.exceptions import ResourceNotFoundError, ValidationError
from tests.base import PlivoPhlosResourceTestCase
from tests.decorators import with_response


class PhlosMemberTest(PlivoPhlosResourceTestCase):

    @with_response(404)
    def test_phlo_get(self):
        """
            for wrong phlo_id validation test case
        """
        with self.assertRaises(ResourceNotFoundError):
            self.client.phlo.get('40b2fa01-39a1-43c8-9f6c-xxxxxxxxxxxx')

        with self.assertRaises(ResourceNotFoundError):
            self.client.phlo.get(12345)

        with self.assertRaises(ResourceNotFoundError):
            phlo_get = self.client.phlo.get('40b2fa01-39a1-43c8-9f6c-7e6a219afe43')
            phlo_get.node('conference_bridge', '5c698012954a4399a455eadd')

        with self.assertRaises(ResourceNotFoundError):
            phlo_get = self.client.phlo.get('40b2fa01-39a1-43c8-9f6c-7e6a219afe43')
            phlo_get.multi_party_call('5c698012954a4399a455eadd')

        with self.assertRaises(ResourceNotFoundError):
            phlo_get = self.client.phlo.get('40b2fa01-39a1-43c8-9f6c-7e6a219afe43')
            phlo_get.run()

    @with_response(400)
    def test_phlo_get_validation(self):
        """
            for wrong phlo_id validation test case
        """
        with self.assertRaises(ValidationError):
            self.client.phlo.get(12345)

        with self.assertRaises(ValidationError):
            self.client.phlo.get(None)

        with self.assertRaises(ValidationError):
            phlo_get = self.client.phlo.get('40b2fa01-39a1-43c8-9f6c-7e6a219afe43')
            phlo_get.node('conference_bridge', '5c698012954a4399a455eadd')

        with self.assertRaises(ValidationError):
            phlo_get = self.client.phlo.get('40b2fa01-39a1-43c8-9f6c-7e6a219afe43')
            phlo_get.multi_party_call('5c698012954a4399a455eadd')

        with self.assertRaises(ValidationError):
            phlo_get = self.client.phlo.get('40b2fa01-39a1-43c8-9f6c-7e6a219afe43')
            phlo_get.run()

    @with_response(404)
    def test_member_actions(self):
        with self.assertRaises(ResourceNotFoundError):
            self.client.phlo.member(
                '40b2fa01-39a1-43c8-9f6c-7e6a219afe43',
                '5c698012954a4399a455eadd',
                '656432-xxxxx-xxxxx-xxxxx',
                'hold'
            )

        with self.assertRaises(ResourceNotFoundError):
            self.client.phlo.member(
                12345,
                '5c698012954a4399a455eadd',
                '656432-xxxxx-xxxxx-xxxxx',
                'hold'
            )

    @with_response(400)
    def test_member_actions_validation(self):
        with self.assertRaises(ValidationError):
            self.client.phlo.member(
                '40b2fa01-39a1-43c8-9f6c-7e6a219afe43',
                '5c698012954a4399a455eadd',
                '656432-xxxxx-xxxxx-xxxxx',
                'hold'
            )

        with self.assertRaises(ValidationError):
            self.client.phlo.member(
                '40b2fa01-39a1-43c8-9f6c-7e6a219afe43',
                '5c698012954a4399a455eadd',
                '656432-xxxxx-xxxxx-xxxxx',
                'mute'
            )
