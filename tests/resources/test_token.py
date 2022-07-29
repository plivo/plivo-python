# -*- coding: utf-8 -*-

from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class TokenTest(PlivoResourceTestCase):
    @with_response(503)
    @with_response(503)
    @with_response(201)
    def test_create(self):
        self.client.token.create(
            iss = "MAMDVLZJY2ZGY5MWU1ZJ",
            sub = "kowshik",
            nbf = "1659078396",
            exp = "1659088396",
            incoming_allow = False,
            outgoing_allow = False,
            app = "app"
            )
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('JWT/Token'), self.client.current_request.url)