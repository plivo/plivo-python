from plivo import exceptions
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class MediaTest(PlivoResourceTestCase):
    @with_response(200)
    def test_get_media(self):
        media_id = 'media_id'
        media = self.client.media.get(media_id)
        self.assertResponseMatches(media)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Media', media_id))
        self.assertEqual(self.client.current_request.method, 'GET')

    @with_response(200)
    def test_list(self):
        media = self.client.media.list()
        # Test if ListResponseObject's __iter__ is working correctly
        self.assertEqual(len(list(media)), 20)
        self.assertUrlEqual(self.client.current_request.url,
                            self.get_url('Media'))
        self.assertEqual(self.client.current_request.method, 'GET')
