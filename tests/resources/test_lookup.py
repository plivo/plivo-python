from plivo import exceptions
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class LookupTest(PlivoResourceTestCase):
    @with_response(200)
    def test_get(self):
        number = '+14154305555'
        resp = self.client.lookup.get(number)
        self.assertResponseMatches(resp)
        self.assertEqual(self.client.current_request.method, 'GET')
