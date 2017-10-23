# -*- coding: utf-8 -*-
from unittest import TestCase

from plivo import plivoxml


class PlivoXMLTest(TestCase):
    def test_simple(self):
        self.assertEqual(plivoxml.ResponseElement().to_string(),
                         '<Response></Response>\n')

    def test_complex(self):
        self.assertEqual(
            plivoxml.ResponseElement()
            .add(plivoxml.MessageElement('text', '123', '456'))
            .add(plivoxml.ConferenceElement('name'))
            .add(plivoxml.DTMFElement('123')).add(plivoxml.WaitElement())
            .add(plivoxml.SpeakElement('Hello'))
            .add(plivoxml.PreAnswerElement().add_speak('Hello'))
            .add(plivoxml.PlayElement('url'))
            .add(plivoxml.DialElement().set_caller_name('Test').add(
                plivoxml.NumberElement('123').set_send_on_preanswer(
                    True))).to_string(),
            '<Response><Message dst="456" src="123">text</Message><Conference>name</Conference><DTMF>123</DTMF><Wait></Wait><Speak>Hello</Speak><PreAnswer><Speak>Hello</Speak></PreAnswer><Play>url</Play><Dial callerName="Test"><Number sendOnPreanswer="true">123</Number></Dial></Response>\n'
        )
