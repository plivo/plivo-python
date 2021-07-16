from unittest import TestCase

from plivo import plivoxml
from tests import PlivoXmlTestCase


class BreakElementTest(TestCase, PlivoXmlTestCase):
    def test_set_methods(self):
        time = "1000ms"
        strength = "x-strong"
        expected_response = '<Response><Speak voice="Polly.Joey">Break of<break strength="x-strong" time="1000ms"/> one second or same as paragraph </Speak></Response>'
        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.SpeakElement("Break of", "Polly.Joey").add(
                plivoxml.BreakElement().set_strength(strength).set_time(time)
            ).add_cont("one second or same as paragraph")
        ).to_string(False)
        self.assertXmlEqual(response, expected_response)
