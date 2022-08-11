# -*- coding: utf-8 -*-
from tests import PlivoResourceTestCase
from tests.decorators import with_response


class TokenTest(PlivoResourceTestCase):
    @with_response(200)
    def test_create(self):
        self.client.token.create("MAMDVLZJY2ZGY5MWU1ZJ")
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('JWT/Token'), self.client.current_request.url)
