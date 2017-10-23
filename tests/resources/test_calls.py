# -*- coding: utf-8 -*-

from tests.base import PlivoResourceTestCase
from tests.decorators import with_response

uuid = '4d04c52e-cea3-4458-bbdb-0bfc314ee7cd'


class CallTest(PlivoResourceTestCase):
    @with_response(200)
    def test_create(self):
        self.client.calls.create(
            from_='1231231230',
            to_='3213213210',
            answer_url='http://www.example.com')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Call'), self.client.current_request.url)

    @with_response(200)
    def test_list(self):
        self.client.calls.list()
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.get_url('Call', limit=20, offset=0),
            self.client.current_request.url)

    @with_response(200)
    def test_get(self):
        uuid = '4d04c52e-cea3-4458-bbdb-0bfc314ee7cd'
        call = self.client.calls.get(uuid)
        self.assertResponseMatches(call)
        self.assertEqual(self.client.current_request.method, 'GET')
        self.assertUrlEqual(
            self.get_url('Call', uuid), self.client.current_request.url)

    @with_response(202)
    def test_update(self):
        uuid = '4d04c52e-cea3-4458-bbdb-0bfc314ee7cd'
        self.client.calls.update(
            uuid, legs='aleg', aleg_url='http://www.example.com')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Call', uuid), self.client.current_request.url)


class LiveCallTest(PlivoResourceTestCase):
    @with_response(202)
    def test_play_create(self):
        self.client.calls.play(uuid, 'http://test.url')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Call', uuid, 'Play'),
            self.client.current_request.url)

    @with_response(204)
    def test_play_delete(self):
        self.client.calls.play_stop(uuid)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Call', uuid, 'Play'),
            self.client.current_request.url)

    @with_response(202)
    def test_record_create(self):
        self.client.calls.record(uuid, 'http://test.url')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Call', uuid, 'Record'),
            self.client.current_request.url)

    @with_response(204)
    def test_record_delete(self):
        self.client.calls.record_stop(uuid)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Call', uuid, 'Record'),
            self.client.current_request.url)

    @with_response(202)
    def test_dtmf_create(self):
        self.client.calls.send_digits(uuid, '123')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Call', uuid, 'DTMF'),
            self.client.current_request.url)

    @with_response(202)
    def test_play_create(self):
        self.client.calls.play(uuid, 'http://test.url')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Call', uuid, 'Play'),
            self.client.current_request.url)

    @with_response(204)
    def test_play_delete(self):
        self.client.calls.play_stop(uuid)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Call', uuid, 'Play'),
            self.client.current_request.url)

    @with_response(202)
    def test_speak_create(self):
        self.client.calls.speak(uuid, 'http://test.url')
        self.assertEqual(self.client.current_request.method, 'POST')
        self.assertUrlEqual(
            self.get_url('Call', uuid, 'Speak'),
            self.client.current_request.url)

    @with_response(204)
    def test_speak_delete(self):
        self.client.calls.speak_stop(uuid)
        self.assertEqual(self.client.current_request.method, 'DELETE')
        self.assertUrlEqual(
            self.get_url('Call', uuid, 'Speak'),
            self.client.current_request.url)
