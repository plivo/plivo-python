# -*- coding: utf-8 -*-

from datetime import datetime

import plivo
from tests.base import PlivoResourceTestCase
from tests.decorators import with_response


class TranscriptionTest(PlivoResourceTestCase):
    @with_response(200)
    def test_get(self):

        transcription = self.client.transcriptions.get_tanscription(
            'ac28a19f-dc24-40ad-9745-7c29ee3f2c46')

        self.assertResponseMatches(transcription)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Transcription/ac28a19f-dc24-40ad-9745-7c29ee3f2c46/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('GET', self.client.current_request.method)

        self.assertEqual('\nSpeaker 0: Scan just to be safe. If you notice any error messages, please let me know immediately. They can help us diagnose the issue better. If it continues to freeze, we might need to look into your system performance. I can guide you through checking your task manager if that helps.\n\nSometimes, background processes can use up a lot of resources. I under', transcription.transcription)

    def test_create(self):
        transcription = self.client.transcriptions.create_tanscription(
            'ac28a19f-dc24-40ad-9745-7c29ee3f2c46')

        self.assertResponseMatches(transcription)

        # Verifying the endpoint hit
        self.assertEqual(
            'https://api.plivo.com/v1/Account/MAXXXXXXXXXXXXXXXXXX/Transcription/ac28a19f-dc24-40ad-9745-7c29ee3f2c46/',
            self.client.current_request.url)

        # Verifying the method used
        self.assertEqual('POST', self.client.current_request.method)

        self.assertEqual('transcription in progress',transcription.message)