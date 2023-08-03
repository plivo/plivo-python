from tests.base import PlivoResourceTestCase
from tests.decorators import with_response

class MaskingSessionTest(PlivoResourceTestCase):
    @with_response(201)
    def test_create(self):
        self.client.masking_sessions.create_masking_session(
            first_party='917708772011',
            second_party='918220568648')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('Masking', 'Session'), self.client.current_request.url)

    @with_response(200)
    def test_delete(self):
        session_uuid = "9fe6cba9-62b2-4de0-98a4-6b878fb906de"
        self.client.masking_sessions.delete_masking_session(
            session_uuid)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_voice_url('Masking', 'Session', session_uuid), self.client.current_request.url)

    @with_response(200)
    def test_get(self):
        session_uuid = "c2146ba4-798d-49b0-8580-53851a16e055"
        self.client.masking_sessions.get_masking_session(session_uuid)
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.get_voice_url('Masking', 'Session', session_uuid), self.client.current_request.url)

    @with_response(200)
    def test_update(self):
        session_uuid = "7b5c5e17-e1e9-4ccd-a480-42f5c97fbe96"
        self.client.masking_sessions.update_masking_session(
            session_uuid=session_uuid,
            call_time_limit=14600,
            record=True)
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('Masking', 'Session', session_uuid), self.client.current_request.url)

    @with_response(200)
    def test_list(self):
        self.client.masking_sessions.list_masking_session(
            duration__gte=50,
            status="expired")
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.get_voice_url('Masking', 'Session', duration__gte=50,
                               status="expired"), self.client.current_request.url)