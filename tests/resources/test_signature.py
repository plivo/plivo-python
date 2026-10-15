# -*- coding: utf-8 -*-

import binascii

import plivo
from plivo.utils.signature_v3 import construct_post_url, get_signature_v3
from tests.base import PlivoResourceTestCase


class SignatureTest(PlivoResourceTestCase):
    def test_signature(self):
        self.assertEqual(True,
                         plivo.utils.validate_signature(
                             'https://answer.url', '12345',
                             'ehV3IKhLysWBxC1sy8INm0qGoQYdYsHwuoKjsX7FsXc=',
                             'my_auth_token'))

        self.assertEqual(False,
                         plivo.utils.validate_signature(
                             'https://answer.url', '12345',
                             'ehV3IKhLysWBxC1sy8INm0qGoQYdYsHwuoKjsX7FsXc=',
                             'my_auth_tokens'))


SCOPED_TOKEN_1 = 'PLV' + 'obLD1OX2BxgpOktcbX6PkBEiM0RVZneImaq7zN3u_wA'
SCOPED_TOKEN_2 = 'PLV' + 'A' * 43
SCOPED_NONCE = '01456268273535255990'
SCOPED_POST_URL = 'https://acme.example.com/sms/status'
SCOPED_GET_SIG = 'nr+QWHZTVoEP0rWEEWMeWjgKRzfOOuBhJvJqQQ8ZC2s='
SCOPED_POST_SIG = 'Kxo1ZuQEWE578HnfEhiJvLjXNzZXYPvkZDKNq9s4kvk='


def scoped_post_params(status='delivered'):
    return {'MessageUUID': '6f1c2a90-0d7e-4b1e-9c11-1d2e3f4a5b6c', 'Status': status, 'To': '14155550100'}


class ScopedSignatureV3Test(PlivoResourceTestCase):
    def test_derive_signing_key(self):
        self.assertEqual('e55b316ef14f5830de74d2cc2ae794b87c6c349f577d2fabd648884afba6c7ca',
                         binascii.hexlify(plivo.utils.derive_signing_key(SCOPED_TOKEN_1)).decode('ascii'))
        self.assertEqual('c89d8ad56ac99e1a8def8cecce07ffb55332fe813673be81df8b1297d1206368',
                         binascii.hexlify(plivo.utils.derive_signing_key(SCOPED_TOKEN_2)).decode('ascii'))

    def test_validate_v3_signature_scoped(self):
        validate = plivo.utils.validate_v3_signature_scoped
        self.assertTrue(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, SCOPED_TOKEN_1, SCOPED_POST_SIG,
                                 scoped_post_params()))
        self.assertTrue(validate('GET', 'https://acme.example.com/answer?From=14155550100&CallUUID=abc', SCOPED_NONCE,
                                 SCOPED_TOKEN_1, SCOPED_GET_SIG))
        self.assertTrue(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, SCOPED_TOKEN_1, 'bogus,' + SCOPED_POST_SIG,
                                 scoped_post_params()))
        self.assertFalse(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, SCOPED_TOKEN_2, SCOPED_POST_SIG,
                                  scoped_post_params()))
        self.assertFalse(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, SCOPED_TOKEN_1, SCOPED_POST_SIG,
                                  scoped_post_params('failed')))
        self.assertFalse(plivo.utils.validate_v3_signature('POST', SCOPED_POST_URL, SCOPED_NONCE, SCOPED_TOKEN_1,
                                                           SCOPED_POST_SIG, scoped_post_params()))

    def test_validate_v3_signature_scoped_multiple_keys(self):
        validate = plivo.utils.validate_v3_signature_scoped
        auth_token = 'test-auth-token'
        base_url = construct_post_url(SCOPED_POST_URL, scoped_post_params()).decode('utf-8')
        auth_sig = get_signature_v3(auth_token.encode('utf-8'), base_url, SCOPED_NONCE.encode('utf-8')).decode('ascii')
        keys = [SCOPED_TOKEN_1, auth_token]
        self.assertTrue(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, keys, SCOPED_POST_SIG, scoped_post_params()))
        self.assertTrue(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, keys, auth_sig, scoped_post_params()))
        self.assertTrue(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, [SCOPED_TOKEN_2, auth_token],
                                 SCOPED_POST_SIG + ',' + auth_sig, scoped_post_params()))
        self.assertFalse(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, [SCOPED_TOKEN_2], SCOPED_POST_SIG,
                                  scoped_post_params()))
        self.assertFalse(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, [], SCOPED_POST_SIG, scoped_post_params()))
        self.assertTrue(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, [None, '', SCOPED_TOKEN_1], SCOPED_POST_SIG,
                                 scoped_post_params()))
        self.assertTrue(validate('POST', SCOPED_POST_URL, SCOPED_NONCE, auth_token, auth_sig, scoped_post_params()))
