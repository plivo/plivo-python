# -*- coding: utf-8 -*-

from unittest import TestCase

from plivo import plivoxml


class ResponseElementTest(TestCase):
    def test_create_response(self):
        self.assertEqual(plivoxml.ResponseElement().to_string(),
                         '<Response></Response>\n')

    def test_add_conference(self):
        content = 'test'
        elem = plivoxml.ResponseElement().add_conference(
            content=content).to_string()
        self.assertEqual(
            elem, '<Response><Conference>test</Conference></Response>\n')

    def test_add_dial(self):
        time = 2
        elem = plivoxml.ResponseElement().add_dial(time_limit=time).to_string()
        self.assertEqual(elem,
                         '<Response><Dial timeLimit="2"></Dial></Response>\n')

    def test_add_dtmf(self):
        content = 'dummy'
        elem = plivoxml.ResponseElement().add_dtmf(content=content).to_string()
        self.assertEqual(elem, '<Response><DTMF>dummy</DTMF></Response>\n')

    def test_add_get_digits(self):
        content = 2
        elem = plivoxml.ResponseElement().add_get_digits(
            timeout=content).to_string()
        self.assertEqual(
            elem, '<Response><GetDigits timeout="2"></GetDigits></Response>\n')

    def test_add_hangup(self):
        content = 'dummy'
        elem = plivoxml.ResponseElement().add_hangup(
            reason=content).to_string()
        self.assertEqual(
            elem, '<Response><Hangup reason="dummy"></Hangup></Response>\n')

    def test_add_message(self):
        content = 'dummy'
        elem = plivoxml.ResponseElement().add_message(
            content=content).to_string()
        self.assertEqual(elem,
                         '<Response><Message>dummy</Message></Response>\n')

    def test_add_play(self):
        content = 'dummy'
        elem = plivoxml.ResponseElement().add_play(content=content).to_string()
        self.assertEqual(elem, '<Response><Play>dummy</Play></Response>\n')

    def test_add_pre_answer(self):
        elem = plivoxml.ResponseElement().add_pre_answer().to_string()
        self.assertEqual(elem,
                         '<Response><PreAnswer></PreAnswer></Response>\n')

    def test_add_record(self):
        action = 'https://foo.example.com'
        elem = plivoxml.ResponseElement().add_record(action=action).to_string()
        expected_response = '<Response><Record action="https://foo.example.com"></Record></Response>\n'
        self.assertEqual(elem, expected_response)

    def test_add_redirect(self):
        content = 'dummy'
        elem = plivoxml.ResponseElement().add_redirect(
            content=content).to_string()
        self.assertEqual(elem,
                         '<Response><Redirect>dummy</Redirect></Response>\n')

    def test_add_speak(self):
        response = plivoxml.ResponseElement()
        response.add(
            plivoxml.SpeakElement(
                'Please leave a message after the beep. Press the star key when done.'
            ))
        response.add(
            plivoxml.RecordElement(
                action='http://foo.com/get_recording/',
                max_length=30,
                finish_on_key='*'))
        response.add(plivoxml.SpeakElement('Recording not received.'))
        elem = response.to_string()
        self.assertEqual(
            elem,
            '<Response><Speak>Please leave a message after the beep. Press the star key when done.</Speak><Record action="http://foo.com/get_recording/" finishOnKey="*" maxLength="30"></Record><Speak>Recording not received.</Speak></Response>\n'
        )

    def test_add_wait(self):
        content = 2
        elem = plivoxml.ResponseElement().add_wait(length=content).to_string()
        self.assertEqual(elem,
                         '<Response><Wait length="2"></Wait></Response>\n')
