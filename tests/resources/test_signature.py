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
