# -*- coding: utf-8 -*-

import plivo
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


V3_NONCE = '12345678901234567890'
V3_AUTH_TOKEN = 'test-auth-token'


class SignatureV3Test(PlivoResourceTestCase):
    def test_v3_signature_https_get_unchanged(self):
        self.assertEqual(True,
                         plivo.utils.validate_v3_signature(
                             'GET', 'https://example.com/answer?b=2&a=1', V3_NONCE, V3_AUTH_TOKEN,
                             'HluExHgAFlS85zbkyPGdu74LyNEfFDqs60mE34TFbdQ='))

    def test_v3_signature_https_post_unchanged(self):
        self.assertEqual(True,
                         plivo.utils.validate_v3_signature(
                             'POST', 'https://example.com/answer?b=2&a=1', V3_NONCE, V3_AUTH_TOKEN,
                             'ZzLkHpmvSRaYNUSnpb5wXY5X9Y+RD572Fu5BPX8nVsM=',
                             {'CallUUID': 'abc', 'From': '14155550100'}))

    def test_v3_signature_http_post_unchanged(self):
        self.assertEqual(True,
                         plivo.utils.validate_v3_signature(
                             'POST', 'http://example.com/answer', V3_NONCE, V3_AUTH_TOKEN,
                             'Fu/TqrInsE+jdOWvNgZVOs71Yq4gJ/JCzPUoDNA4pF8=',
                             {'CallUUID': 'abc', 'From': '14155550100'}))

    def test_v3_signature_wss_with_query(self):
        self.assertEqual(True,
                         plivo.utils.validate_v3_signature(
                             'GET', 'wss://example.com/media/stream?tenant=42&env=prod', V3_NONCE, V3_AUTH_TOKEN,
                             'Ni6eSQI9zg/LjUt95Nlt5nTYA7FpL6CQuY2F+Yy3jyc='))

    def test_v3_signature_wss_without_query(self):
        self.assertEqual(True,
                         plivo.utils.validate_v3_signature(
                             'GET', 'wss://example.com/media/stream', V3_NONCE, V3_AUTH_TOKEN,
                             'paNuAIW+AAlyCT4lFH8ZrCvzj3gkNuvrX0r877mN3nM='))

    def test_v3_signature_ws_with_query(self):
        self.assertEqual(True,
                         plivo.utils.validate_v3_signature(
                             'GET', 'ws://example.com/media/stream?tenant=42&env=prod', V3_NONCE, V3_AUTH_TOKEN,
                             'De3cjnXuPrS4pSTyrva6wFEYh9CpRgvlyaQ1gct9auo='))

    def test_v3_signature_ws_without_query(self):
        self.assertEqual(True,
                         plivo.utils.validate_v3_signature(
                             'GET', 'ws://example.com/media/stream', V3_NONCE, V3_AUTH_TOKEN,
                             'jix7ENJwUDNYvxC3AU548c2sk/+8ZDdTt+sFPs1+jg4='))

    def test_v3_signature_wss_second_of_rotated_signatures(self):
        self.assertEqual(True,
                         plivo.utils.validate_v3_signature(
                             'GET', 'wss://example.com/media/stream', V3_NONCE, V3_AUTH_TOKEN,
                             'bm90LXRoZS1zaWduYXR1cmU=,paNuAIW+AAlyCT4lFH8ZrCvzj3gkNuvrX0r877mN3nM='))

    def test_v3_signature_wss_wrong_token(self):
        self.assertEqual(False,
                         plivo.utils.validate_v3_signature(
                             'GET', 'wss://example.com/media/stream', V3_NONCE, 'other-auth-token',
                             'paNuAIW+AAlyCT4lFH8ZrCvzj3gkNuvrX0r877mN3nM='))

    def test_v3_signature_percent_encoded_utf8_query(self):
        self.assertEqual(True,
                         plivo.utils.validate_v3_signature(
                             'GET', 'wss://example.com/s?name=Jos%C3%A9', V3_NONCE, V3_AUTH_TOKEN,
                             'j0fffZVummAvqXtvGPkEVhnNDmDeFaTPXDP4CedUaow='))

    def test_v3_signature_rejects_other_schemes(self):
        with self.assertRaises(plivo.exceptions.ValidationError):
            plivo.utils.validate_v3_signature(
                'GET', 'ftp://example.com/media/stream', V3_NONCE, V3_AUTH_TOKEN,
                'paNuAIW+AAlyCT4lFH8ZrCvzj3gkNuvrX0r877mN3nM=')
