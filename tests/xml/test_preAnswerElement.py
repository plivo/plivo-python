from unittest import TestCase

from plivo import plivoxml
from tests import PlivoXmlTestCase


class PreAnswerElementTest(TestCase, PlivoXmlTestCase):
    def test_set_methods(self):
        expected_response = '<Response><PreAnswer><Speak language="en-US" loop="2" voice="WOMAN">This is test' \
                            '</Speak><Play loop="2">This is test</Play><Wait beep="true" length="1" ' \
                            'minSilence="1" silence="true"/><GetDigits ' \
                            'action="http://www.foo.com/gather_pin/" digitTimeout="2" finishOnKey="#" ' \
                            'invalidDigitsSound="https://s3.amazonaws.com/Trumpet.mp3" log="true" ' \
                            'method="POST" numDigits="1" playBeep="true" redirect="true" retries="1" ' \
                            'timeout="5" validDigits="1234567890*#"/><Redirect method="POST">' \
                            'This is test</Redirect><Message callbackMethod="GET" ' \
                            'callbackUrl="http://foo.example.com" dst="1203443444&lt;1203443445" ' \
                            'src="1202322222" type="sms">this is test</Message><DTMF async="true">this is test' \
                            '</DTMF></PreAnswer></Response>'

        content_speak = 'This is test'
        voice_speak = 'WOMAN'
        language_speak = 'en-US'
        loop_speak = 2
        loop_play = 2
        content_play = 'This is test'
        length_wait=1
        silence_wait=True
        min_silence_wait=1
        beep_wait=True

        action_get_digits = 'http://www.foo.com/gather_pin/'
        method_get_digits = 'POST'
        timeout_get_digits = 5
        digit_timeout_get_digits = 2
        finish_on_key_get_digits = '#'
        num_digits_get_digits = 1
        retries_get_digits = 1
        redirect_get_digits = True
        play_beep_get_digits = True
        valid_digits_get_digits = '1234567890*#'
        invalid_digits_sound_get_digits = 'https://s3.amazonaws.com/Trumpet.mp3'
        log_get_digits = True

        content_redirect = 'This is test'
        method_redirect = "POST"

        src_message = '1202322222'
        dst_message = '1203443444<1203443445'
        type_message = 'sms'
        callback_url_message = 'http://foo.example.com'
        callback_method_message = 'GET'
        content_message = 'this is test'

        content_dtmf = 'this is test'
        async_dtmf = True

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.PreAnswerElement().add_speak(
                content=content_speak,
                voice=voice_speak,
                language=language_speak,
                loop=loop_speak
            ).add_play(
                content=content_play,
                loop=loop_play
            ).add_wait(
                length=length_wait,
                silence=silence_wait,
                min_silence=min_silence_wait,
                beep=beep_wait,
            ).add_get_digits(
                action=action_get_digits,
                method=method_get_digits,
                timeout=timeout_get_digits,
                digit_timeout=digit_timeout_get_digits,
                finish_on_key=finish_on_key_get_digits,
                num_digits=num_digits_get_digits,
                retries=retries_get_digits,
                redirect=redirect_get_digits,
                play_beep=play_beep_get_digits,
                valid_digits=valid_digits_get_digits,
                invalid_digits_sound=invalid_digits_sound_get_digits,
                log=log_get_digits,
            ).add_redirect(
                content=content_redirect,
                method=method_redirect,
            ).add_message(
                content=content_message,
                src=src_message,
                dst=dst_message,
                type=type_message,
                callback_url=callback_url_message,
                callback_method=callback_method_message,
            ).add_dtmf(
                content=content_dtmf,
                async_=async_dtmf,
            )
        ).to_string(False)

        self.assertXmlEqual(response, expected_response)
