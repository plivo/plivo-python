from unittest import TestCase
from plivo import plivoxml


class GetDigitsElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><GetDigits action="https://foo.example.com" digitTimeout="10"' \
            ' finishOnKey="#" invalidDigitsSound="http://foo.audio.url" log="true" method="GET"' \
            ' numDigits="2" playBeep="false" redirect="false" retries="1" timeout="100"' \
            ' validDigits="*"><Speak language="en-US" loop="2" voice="WOMAN">This is test</Speak>' \
            '<Play loop="2">This is test</Play></GetDigits></Response>'

        action = 'https://foo.example.com'
        method = 'GET'
        timeout = 100
        digitTimeout = 10
        finishOnKey = '#'
        numDigits = 2
        retries = True
        redirect = False
        playBeep = False
        validDigits = '*'
        invalidDigitsSound = 'http://foo.audio.url'
        log = True

        content_speak = 'This is test'
        voice_speak = 'WOMAN'
        language_speak = 'en-US'
        loop_speak = 2
        loop_play = 2
        content_play = 'This is test'

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.GetDigitsElement().set_action(action).set_method(method).
            set_redirect(redirect).set_timeout(timeout).set_play_beep(playBeep)
            .set_finish_on_key(finishOnKey).set_digit_timeout(digitTimeout).
            set_timeout(timeout).set_num_digits(numDigits).set_retries(retries)
            .set_valid_digits(validDigits).set_invalid_digits_sound(
                invalidDigitsSound).set_log(log).add_speak(
                    content=content_speak,
                    voice=voice_speak,
                    language=language_speak,
                    loop=loop_speak).add_play(
                        content=content_play, loop=loop_play)).to_string()
        self.assertEqual(response, expected_response + '\n')
