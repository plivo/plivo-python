# -*- coding: utf-8 -*-

import plivo
import time
from tests.base import PlivoResourceTestCase
from plivo.utils import jwt


class AccessTokenTest(PlivoResourceTestCase):
    def test_jwt_constructor(self):
        self.assertRaisesRegexp(TypeError, "", jwt.AccessToken,
                               'ADADADADADADADADADA',
                               'qwerty')

    def test_jwt_constructor_auth_id(self):
        self.assertRaisesRegexp(plivo.exceptions.ValidationError,
                               "auth_id should match format .*",
                               jwt.AccessToken,
                               'ADADADADADADADADADA', 'qwerty', 'username')

    def test_jwt_constructor_auth_id(self):
        self.assertRaisesRegexp(plivo.exceptions.ValidationError,
                               "auth_id should match format .*",
                               jwt.AccessToken,
                               'ADADADADADADADADADA', 'qwerty', 'username')

    def test_jwt_constructor_lifetime(self):
        self.assertRaisesRegexp(plivo.exceptions.ValidationError,
                               ".* lifetime .*",
                               jwt.AccessToken,
                               'MADADADADADADADADADA',
                               'qwerty',
                               'username',
                               valid_from=int(time.time()),
                               lifetime=123)

    def test_jwt_constructor_validity(self):
        self.assertRaisesRegexp(plivo.exceptions.ValidationError,
                               "use either lifetime or valid_till",
                               jwt.AccessToken,
                               'MADADADADADADADADADA',
                               'qwerty',
                               'username',
                               valid_from=int(time.time()),
                               valid_till=int(time.time()) - 100,
                               lifetime=1200)
        self.assertRaisesRegexp(plivo.exceptions.ValidationError,
                               "validity expires .* seconds before it starts",
                               jwt.AccessToken,
                               'MADADADADADADADADADA',
                               'qwerty',
                               'username',
                               valid_from=int(time.time()),
                               valid_till=int(time.time()) - 100)

    def test_jwt(self):
        token = jwt.AccessToken('MADADADADADADADADADA', 'qwerty', 'username', valid_from=12121212, lifetime=300, uid='username-12345')
        token.add_voice_grants(True, True)
        self.assertEqual(True, token.grants['voice']['incoming_allow'])
        self.assertNotEqual(False, token.grants['voice']['outgoing_allow'])
