# -*- coding: utf-8 -*-

from datetime import datetime

import plivo
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class TranscriptionTest(PlivoResourceTestCase):
    @with_response(200)
    def test_get(self):

        transcription = self.client.transcriptions.get_transcription('e12d05fe-6979-485c-83dc-9276114dba3b')

        self.assertResponseMatches(transcription)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Transcription/e12d05fe-6979-485c-83dc-9276114dba3b/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        self.assertEqual('\nSpeaker 0: Scan just to be safe. If you notice any error messages, please let me know immediately. They can help us diagnose the issue better. If it continues to freeze, we might need to look into your system performance. I can guide you through checking your task manager if that helps.\n\nSometimes, background processes can use up a lot of resources. I under', transcription.transcription)

    @with_response(201)
    def test_create(self):
        self.client.transcriptions.create_transcription(
            recording_id='8605287e-1e1a-4341-8235-23574357d6f1')

        # self.assertResponseMatches(transcription)

        # Verifying the endpoint hit
        # self.assertUrlEqual(
        #     self.get_voice_url('Transcription',  '8605287e-1e1a-4341-8235-23574357d6f1'), self.client.current_request.url)
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Transcription/8605287e-1e1a-4341-8235-23574357d6f1/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

        # self.assertEqual('transcription in progress',transcription.message)

    @with_response(202)
    def test_delete(self):
        transcription = self.client.transcriptions.delete_transcription(
            '8605287e-1e1a-4341-8235-23574357d6f1')

        self.assertResponseMatches(transcription)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Transcription/8605287e-1e1a-4341-8235-23574357d6f1/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('DELETE', self.client.current_request.method)

        self.assertEqual('request accepted', transcription.message)