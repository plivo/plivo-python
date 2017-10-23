# -*- coding: utf-8 -*-
from tests.decorators import with_response

from .. import PlivoResourceTestCase

conference_name = 'My Conf Room'
member_id = 'Test Member ID'


class ConferenceTest(PlivoResourceTestCase):
    @with_response(200)
    def test_get(self):
        conference = self.client.conferences.get(conference_name)
        self.assertResponseMatches(conference)
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name),
            self.client.current_request.url)
        self.assertEqual(conference.conference_name, conference_name)

    @with_response(204)
    def test_delete(self):
        self.client.conferences.delete(conference_name)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name),
            self.client.current_request.url)

    @with_response(204)
    def test_delete_all(self):
        self.client.conferences.delete_all()
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Conference'), self.client.current_request.url)

    @with_response(204, method_name='delete')
    def test_hangup(self):
        self.client.conferences.hangup(conference_name)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name),
            self.client.current_request.url)

    @with_response(204, method_name='delete_all')
    def test_hangup_all(self):
        self.client.conferences.hangup_all()
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Conference'), self.client.current_request.url)

    @with_response(200)
    def test_list(self):
        self.client.conferences.list()
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.get_url('Conference'), self.client.current_request.url)

    @with_response(202)
    def test_record_create(self):
        self.client.conferences.record(
            conference_name=conference_name,
            file_format='mp3',
            transcription_url='http://example.transcription.url')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Record'),
            self.client.current_request.url)

    @with_response(204)
    def test_record_delete(self):
        self.client.conferences.record_stop(conference_name=conference_name)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Record'),
            self.client.current_request.url)


class ConferenceMemberTest(PlivoResourceTestCase):
    @with_response(202)
    def test_deaf_create(self):
        self.client.conferences.member_deaf(
            conference_name=conference_name, member_id=member_id)
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Member', member_id,
                         'Deaf'), self.client.current_request.url)

    @with_response(202)
    def test_speak_create(self):
        self.client.conferences.member_speak(
            conference_name=conference_name,
            member_id=member_id,
            text='Hello World!')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Member', member_id,
                         'Speak'), self.client.current_request.url)

    @with_response(202)
    def test_play_create(self):
        self.client.conferences.member_play(
            conference_name=conference_name,
            member_id=member_id,
            url='http://url.to.sound')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Member', member_id,
                         'Play'), self.client.current_request.url)

    @with_response(202)
    def test_mute_create(self):
        self.client.conferences.member_mute(
            conference_name=conference_name, member_id=member_id)
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Member', member_id,
                         'Mute'), self.client.current_request.url)

    @with_response(204)
    def test_mute_delete(self):
        self.client.conferences.member_mute_stop(
            conference_name=conference_name, member_id=member_id)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Member', member_id,
                         'Mute'), self.client.current_request.url)

    @with_response(204)
    def test_deaf_delete(self):
        self.client.conferences.member_deaf_stop(
            conference_name=conference_name, member_id=member_id)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Member', member_id,
                         'Deaf'), self.client.current_request.url)

    @with_response(204)
    def test_speak_delete(self):
        self.client.conferences.member_speak_stop(
            conference_name=conference_name, member_id=member_id)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Member', member_id,
                         'Speak'), self.client.current_request.url)

    @with_response(204)
    def test_play_delete(self):
        self.client.conferences.member_play_stop(
            conference_name=conference_name, member_id=member_id)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Member', member_id,
                         'Play'), self.client.current_request.url)

    @with_response(202)
    def test_kick_create(self):
        self.client.conferences.member_kick(
            conference_name=conference_name, member_id=member_id)
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Member', member_id,
                         'Kick'), self.client.current_request.url)

    @with_response(204)
    def test_delete(self):
        self.client.conferences.member_hangup(
            conference_name=conference_name, member_id=member_id)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Conference', conference_name, 'Member', member_id),
            self.client.current_request.url)
