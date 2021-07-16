from unittest import TestCase
from plivo import plivoxml
from tests import PlivoXmlTestCase


class GetInputElementTest(TestCase, PlivoXmlTestCase):
    def test_set_methods(self):
        expected_response = '<Response><GetInput action="https://foo.example.com" digitEndTimeout="50" ' \
                            'executionTimeout="100" finishOnKey="#" hints="1 2 3" inputType="speech" ' \
                            'interimSpeechResultsCallback="https://bar.example.com" ' \
                            'interimSpeechResultsCallbackMethod="POST" language="en-US" log="true" method="GET" ' \
                            'numDigits="2" redirect="false" speechEndTimeout="25" ' \
                            'speechModel="default"><Speak language="en-US" loop="2" ' \
                            'voice="WOMAN">This is test</Speak><Play loop="2">This is test' \
                            '</Play></GetInput></Response>'

        action = 'https://foo.example.com'
        method = 'GET'
        inputType = 'speech'
        executionTimeout = 100
        digitEndTimeout = 50
        speechEndTimeout = 25
        finishOnKey = '#'
        numDigits = 2
        speechModel = 'default'
        hints = '1 2 3'
        language = 'en-US'
        interimSpeechResultsCallback = 'https://bar.example.com'
        interimSpeechResultsCallbackMethod = 'POST'
        redirect = False
        log = True

        content_speak = 'This is test'
        voice_speak = 'WOMAN'
        language_speak = 'en-US'
        loop_speak = 2
        loop_play = 2
        content_play = 'This is test'

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.GetInputElement().set_action(action).set_method(method).
            set_input_type(inputType).set_execution_timeout(executionTimeout).
            set_digit_end_timeout(digitEndTimeout).set_speech_end_timeout(speechEndTimeout).
            set_finish_on_key(finishOnKey).set_num_digits(numDigits).
            set_hints(hints).set_interim_speech_results_callback(interimSpeechResultsCallback).
            set_interim_speech_results_callback_method(interimSpeechResultsCallbackMethod).set_log(log).
            set_redirect(redirect).set_language(language).set_speech_model(speechModel).
            add_speak(
                content=content_speak,
                voice=voice_speak,
                language=language_speak,
                loop=loop_speak).add_play(
                content=content_play, loop=loop_play)
        ).to_string(False)
        self.assertXmlEqual(response, expected_response)
