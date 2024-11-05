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

    @with_response(201)
    # geomatch = false
    def test_create(self):
        self.client.masking_sessions.create_masking_session(
            first_party='917708772011',
            second_party='918220568648',
            geomatch=False)
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('Masking', 'Session'), self.client.current_request.url)

    @with_response(201)
    # geomatch = true
    def test_create(self):
        self.client.masking_sessions.create_masking_session(
            first_party='917708772011',
            second_party='918220568648',
            geomatch=True)
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('Masking', 'Session'), self.client.current_request.url)

    @with_response(201)
    # subaccount is passed
    def test_create(self):
        self.client.masking_sessions.create_masking_session(
            first_party='917708772011',
            second_party='918220568648',
            subaccount='SAZTA0ZJJHMDETOWQ4YI')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('Masking', 'Session'), self.client.current_request.url)

    @with_response(201)
    # create_session_with_single_party is passed
    def test_create(self):
        self.client.masking_sessions.create_masking_session(
            first_party='917708772011',
            create_session_with_single_party=True)
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('Masking', 'Session'), self.client.current_request.url)

    @with_response(201)
    # force_pin_authentication is passed
    def test_create(self):
        self.client.masking_sessions.create_masking_session(
            first_party='917708772011',
            second_party='916303955746',
            is_pin_authentication_required=True,
            first_party_pin="1234",
            second_party_pin="4321",
            pin_prompt_play="https://file-examples.com/storage/fefda3519566d3360a0efb3/2017/11/file_example_MP3_700KB.mp3",
            pin_retry=2,
            pin_retry_wait=7,
            incorrect_pin_play="https://file-examples.com/storage/fefda3519566d3360a0efb3/2017/11/file_example_MP3_700KB.mp3",
            unknown_caller_play="https://file-examples.com/storage/fefda3519566d3360a0efb3/2017/11/file_example_MP3_700KB.mp3",
            force_pin_authentication=True,
            session_expiry=0)
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_voice_url('Masking', 'Session'), self.client.current_request.url)

    @with_response(201)
    # virtual_number_cooloff_period is passed
    def test_create(self):
        self.client.masking_sessions.create_masking_session(
            first_party='917708772011',
            second_party='916303955746',
            virtual_number_cooloff_period=3500,
            )
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
