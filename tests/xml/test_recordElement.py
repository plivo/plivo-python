from unittest import TestCase
from plivo import plivoxml
from tests import PlivoXmlTestCase


class RecordElementTest(TestCase, PlivoXmlTestCase):
    def test_set_methods(self):
        expected_response = '<Response><Record action="https://foo.example.com" callbackMethod="GET" ' \
                            'callbackUrl="https://foo.example.com" fileFormat="wav" finishOnKey="#" ' \
                            'maxLength="10" method="GET" playBeep="false" recordSession="false" ' \
                            'redirect="false" startOnDialAnswer="false" timeout="100" transcriptionMethod="GET" ' \
                            'transcriptionType="hybrid" transcriptionUrl="https://foo.example.com"/>' \
                            '</Response>'
        action = 'https://foo.example.com'
        method = 'GET'
        fileFormat = 'wav'
        redirect = False
        timeout = 100
        maxLength = 10
        recordSession = False
        startOnDialAnswer = False
        playBeep = False
        finishOnKey = '#'
        transcriptionType = 'hybrid'
        transcriptionUrl = 'https://foo.example.com'
        transcriptionMethod = 'GET'
        callbackUrl = 'https://foo.example.com'
        callbackMethod = 'GET'

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.RecordElement().set_action(action).set_method(method)
            .set_file_format(fileFormat).set_redirect(redirect).set_timeout(
                timeout).set_max_length(maxLength).set_play_beep(playBeep)
            .set_finish_on_key(finishOnKey).set_record_session(recordSession).
            set_start_on_dial_answer(startOnDialAnswer).set_transcription_type(
                transcriptionType).set_transcription_url(transcriptionUrl)
            .set_transcription_method(transcriptionMethod).set_callback_url(
                callbackUrl).set_callback_method(callbackMethod)).to_string(False)
        self.assertXmlEqual(response, expected_response)
