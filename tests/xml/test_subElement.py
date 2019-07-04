from unittest import TestCase

from plivo import plivoxml


class SubElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><Speak>substitution example <sub alias="World Wide Web Consortium">W3C</sub></Speak></Response>'
        alias="World Wide Web Consortium"

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.SpeakElement("substitution example ").add(
                plivoxml.SubElement("W3C").set_alias(alias)
            )
        ).to_string(False)
        self.assertEqual(response, expected_response)
