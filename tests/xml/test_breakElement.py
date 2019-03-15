from unittest import TestCase

from plivo import plivoxml


class BreakElementTest(TestCase):
    def test_set_methods(self):
        time = "250ms"
        strength = "strength"
        expected_response = '<Response><Break strength="strength" time="250ms"/></Response>'
        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.BreakElement().set_strength(strength).set_time(time)
        ).to_string()
        self.assertEqual(response, expected_response + '\n')
