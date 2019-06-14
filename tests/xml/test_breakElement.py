from unittest import TestCase

from plivo import plivoxml


class BreakElementTest(TestCase):
    def test_set_methods(self):
        time = "250ms"
        strength = "strength"
        expected_response = '<Response><Speak><Break strength="strength" time="250ms"/></Speak></Response>'
        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.SpeakElement("").add(
                plivoxml.BreakElement().set_strength(strength).set_time(time)
            )
        ).to_string()
        self.assertEqual(response, expected_response + '\n')
